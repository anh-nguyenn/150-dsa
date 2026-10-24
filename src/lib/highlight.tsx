import type { ReactNode } from 'react'

const KEYWORDS = new Set(
  'False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda match case nonlocal not or pass raise return try while with yield'.split(
    ' ',
  ),
)

const BUILTINS = new Set(
  'abs all any bool bytes callable dict divmod enumerate filter float frozenset getattr hasattr hash hex int isinstance len list map max min next object ord pow print range repr reversed round set slice sorted str sum super tuple type zip'.split(
    ' ',
  ),
)

const TOKEN = /(#[^\n]*)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_]\w*\b)/g

export function highlightLine(line: string, keyPrefix: string | number): ReactNode[] {
  const nodes: ReactNode[] = []
  let last = 0
  let match: RegExpExecArray | null
  TOKEN.lastIndex = 0

  while ((match = TOKEN.exec(line)) !== null) {
    if (match.index > last) nodes.push(line.slice(last, match.index))
    const token = match[0]
    const key = `${keyPrefix}-${match.index}`
    const [, commentToken, stringToken, numberToken, identifierToken] = match

    if (commentToken) {
      nodes.push(
        <span className="tok-comment" key={key}>
          {token}
        </span>,
      )
    } else if (stringToken) {
      nodes.push(
        <span className="tok-string" key={key}>
          {token}
        </span>,
      )
    } else if (numberToken) {
      nodes.push(
        <span className="tok-number" key={key}>
          {token}
        </span>,
      )
    } else if (identifierToken) {
      const rest = line.slice(match.index + token.length)
      const isCall = /^\s*\(/.test(rest)
      if (KEYWORDS.has(token)) {
        nodes.push(
          <span className="tok-keyword" key={key}>
            {token}
          </span>,
        )
      } else if (BUILTINS.has(token)) {
        nodes.push(
          <span className="tok-builtin" key={key}>
            {token}
          </span>,
        )
      } else if (isCall) {
        nodes.push(
          <span className="tok-fn" key={key}>
            {token}
          </span>,
        )
      } else {
        nodes.push(token)
      }
    } else {
      nodes.push(token)
    }
    last = match.index + token.length
  }

  if (last < line.length) nodes.push(line.slice(last))
  return nodes
}
