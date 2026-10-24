import { useEffect, useState } from 'react'
import { highlightLine } from '../lib/highlight'

interface CodeBlockProps {
  code: string
  label?: string
}

export function CodeBlock({ code, label }: CodeBlockProps) {
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    if (!copied) return
    const timer = window.setTimeout(() => setCopied(false), 1600)
    return () => window.clearTimeout(timer)
  }, [copied])

  const lines = code.replace(/\r\n/g, '\n').replace(/\n$/, '').replace(/\t/g, '    ').split('\n')

  async function copy() {
    try {
      await navigator.clipboard.writeText(code)
      setCopied(true)
    } catch {
      setCopied(false)
    }
  }

  return (
    <div className="code-card">
      <div className="code-head">
        <span>{label ?? 'python'}</span>
        <button type="button" className="code-copy" onClick={copy}>
          {copied ? 'Copied' : 'Copy'}
        </button>
      </div>
      <div className="code-scroll">
        <pre className="code">
          {lines.map((line, index) => (
            <span className="code-line" key={index}>
              <span className="ln" aria-hidden="true">
                {index + 1}
              </span>
              <span className="lc">{highlightLine(line, index)}</span>
            </span>
          ))}
        </pre>
      </div>
    </div>
  )
}
