import { useEffect, useRef } from 'react'
import { basicSetup } from 'codemirror'
import { EditorState } from '@codemirror/state'
import { EditorView, keymap } from '@codemirror/view'
import { python } from '@codemirror/lang-python'

interface PythonEditorProps {
  value: string
  onChange: (value: string) => void
  onRun: () => void
}

const theme = EditorView.theme(
  {
    '&': {
      backgroundColor: 'transparent',
      color: 'var(--text)',
      fontSize: '13px',
    },
    '.cm-content': {
      fontFamily: 'var(--mono)',
      padding: '12px 0',
      caretColor: 'var(--accent)',
    },
    '.cm-scroller': {
      fontFamily: 'var(--mono)',
      lineHeight: '1.7',
    },
    '.cm-gutters': {
      backgroundColor: 'transparent',
      borderRight: '1px solid var(--border)',
      color: 'var(--muted)',
    },
    '.cm-activeLine': {
      backgroundColor: 'var(--bg-hover)',
    },
    '.cm-activeLineGutter': {
      backgroundColor: 'transparent',
      color: 'var(--muted)',
    },
    '.cm-selectionBackground, ::selection': {
      backgroundColor: 'var(--accent-dim) !important',
    },
    '&.cm-focused': {
      outline: 'none',
    },
  },
  { dark: false },
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
