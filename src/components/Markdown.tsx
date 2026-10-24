import { useEffect, useMemo, useRef } from 'react'
import { marked } from 'marked'

marked.setOptions({ gfm: true, breaks: false })

interface MarkdownProps {
  children: string
  className?: string
}

export function Markdown({ children, className }: MarkdownProps) {
  const ref = useRef<HTMLDivElement>(null)
  const html = useMemo(() => marked.parse(children, { async: false }) as string, [children])

  useEffect(() => {
    const root = ref.current
    if (!root) return
    root.querySelectorAll('a[href^="http"]').forEach((anchor) => {
      anchor.setAttribute('target', '_blank')
      anchor.setAttribute('rel', 'noreferrer noopener')
    })
  }, [html])

  return (
    <div
      ref={ref}
      className={className ? `prose ${className}` : 'prose'}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  )
}
