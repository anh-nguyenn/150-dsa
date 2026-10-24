import { useEffect, useRef } from 'react'
import { basicSetup } from 'codemirror'
import { EditorState } from '@codemirror/state'
import { EditorView, keymap } from '@codemirror/view'
import { python } from '@codemirror/lang-python'
import { oneDark } from '@codemirror/theme-one-dark'

interface PythonEditorProps {
  value: string
  onChange: (value: string) => void
  onRun: () => void
}

const theme = EditorView.theme(
  {
    '&': {
      backgroundColor: 'transparent',
      color: '#d7d3ca',
      fontSize: '13px',
    },
    '.cm-content': {
      fontFamily: 'var(--mono)',
      padding: '12px 0',
      caretColor: '#d6b477',
    },
    '.cm-scroller': {
      fontFamily: 'var(--mono)',
      lineHeight: '1.7',
    },
    '.cm-gutters': {
      backgroundColor: 'transparent',
      borderRight: '1px solid #24282d',
      color: '#4f575e',
    },
    '.cm-activeLine': {
      backgroundColor: 'rgba(255, 255, 255, 0.022)',
    },
    '.cm-activeLineGutter': {
      backgroundColor: 'transparent',
      color: '#99a1a9',
    },
    '.cm-selectionBackground, ::selection': {
      backgroundColor: 'rgba(214, 180, 119, 0.2) !important',
    },
    '&.cm-focused': {
      outline: 'none',
    },
  },
  { dark: true },
)

export function PythonEditor({ value, onChange, onRun }: PythonEditorProps) {
  const host = useRef<HTMLDivElement>(null)
  const view = useRef<EditorView | null>(null)
  const changeRef = useRef(onChange)
  const runRef = useRef(onRun)

  useEffect(() => {
    changeRef.current = onChange
  }, [onChange])

  useEffect(() => {
    runRef.current = onRun
  }, [onRun])

  useEffect(() => {
    if (!host.current) return
    const instance = new EditorView({
      state: EditorState.create({
        doc: value,
        extensions: [
          basicSetup,
          python(),
          oneDark,
          theme,
          EditorView.lineWrapping,
          EditorView.contentAttributes.of({ 'aria-label': 'Python solution editor', spellcheck: 'false' }),
          keymap.of([
            {
              key: 'Mod-Enter',
              run: () => {
                runRef.current()
                return true
              },
            },
          ]),
          EditorView.updateListener.of((update) => {
            if (update.docChanged) changeRef.current(update.state.doc.toString())
          }),
        ],
      }),
      parent: host.current,
    })
    view.current = instance
    return () => {
      instance.destroy()
      view.current = null
    }
  }, [])

  useEffect(() => {
    const instance = view.current
    if (!instance) return
    const current = instance.state.doc.toString()
    if (current === value) return
    instance.dispatch({
      changes: { from: 0, to: current.length, insert: value },
    })
  }, [value])

  return <div className="editor-host" ref={host} />
}
