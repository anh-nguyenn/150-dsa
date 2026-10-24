import type { Problem } from '../lib/content'
import { Markdown } from './Markdown'

function InlineText({ text }: { text: string }) {
  return (
    <>
      {text.split(/(`[^`]+`)/g).map((part, index) =>
        part.startsWith('`') && part.endsWith('`') ? <code key={index}>{part.slice(1, -1)}</code> : part,
      )}
    </>
  )
}

export function Statement({ problem }: { problem: Problem }) {
  return (
    <div className="statement">
      {problem.summary && <Markdown className="statement-description">{problem.summary}</Markdown>}

      {problem.examples.length > 0 && (
        <div className="examples">
          {problem.examples.map((example, index) => (
            <section className="example-block" key={index} aria-label={`Example ${index + 1}`}>
              <p className="example-label">Example {index + 1}</p>
              {example.body ? (
                <Markdown className="example-body">{example.body}</Markdown>
              ) : (
                <>
                  <div className="example-row">
                    <span className="example-field">Input</span>
                    <pre className="example-value">{example.input}</pre>
                  </div>
                  <div className="example-row">
                    <span className="example-field">Output</span>
                    <pre className="example-value">{example.output}</pre>
                  </div>
                </>
              )}
              {example.explanation && <Markdown className="example-explanation">{example.explanation}</Markdown>}
            </section>
          ))}
        </div>
      )}

      {problem.constraints.length > 0 && (
        <section className="constraints-block" aria-labelledby="constraints-title">
          <h3 className="statement-subhead" id="constraints-title">
            Constraints
          </h3>
          <ul className="constraints">
            {problem.constraints.map((constraint) => (
              <li key={constraint}>
              <InlineText text={constraint} />
            </li>
            ))}
          </ul>
        </section>
      )}

      <a
        className="source-link"
        href={`https://leetcode.com/problems/${problem.meta.slug}/`}
        target="_blank"
        rel="noreferrer noopener"
      >
        Open on LeetCode <span aria-hidden="true">↗</span>
      </a>
    </div>
  )
}
