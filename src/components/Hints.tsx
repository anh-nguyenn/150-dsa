import { useState } from 'react'
import { Markdown } from './Markdown'

interface HintsProps {
  markdown: string
}

function parseHints(markdown: string) {
  return markdown
    .split(/^## /m)
    .filter((chunk) => chunk.trim().length > 0)
    .map((chunk) => {
      const [title, ...rest] = chunk.split('\n')
      return { title: title.trim(), body: rest.join('\n').trim() }
    })
}

export function Hints({ markdown }: HintsProps) {
  const hints = parseHints(markdown)
  const [open, setOpen] = useState<number | null>(null)

  return (
    <div className="hints">
      {hints.map((hint, index) => {
        const isOpen = open === index
        return (
          <div className="hint" key={hint.title}>
            <button
              type="button"
              className="hint-toggle"
              aria-expanded={isOpen}
              aria-controls={`hint-body-${index}`}
              onClick={() => setOpen(isOpen ? null : index)}
            >
              <span className="hint-index">{String(index + 1).padStart(2, '0')}</span>
              <span className="hint-title">{hint.title}</span>
              <span className="hint-action">{isOpen ? 'Hide' : 'Show'}</span>
            </button>
            {isOpen && (
              <div className="hint-body" id={`hint-body-${index}`}>
                <Markdown>{hint.body}</Markdown>
              </div>
            )}
          </div>
        )
      })}
    </div>
  )
}
