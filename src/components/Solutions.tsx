import { useRef, type KeyboardEvent } from 'react'
import { useSearchParams } from 'react-router-dom'
import type { Problem } from '../lib/content'
import { CodeBlock } from './CodeBlock'
import { Markdown } from './Markdown'
import { Visualizer } from './Visualizer'

export function Solutions({ problem }: { problem: Problem }) {
  const [searchParams, setSearchParams] = useSearchParams()
  const requested = searchParams.get('approach')
  const requestedIndex = problem.approaches.findIndex((approach) => approach.meta.id === requested)
  const selected = requestedIndex >= 0 ? requestedIndex : 0
  const tabs = useRef<(HTMLButtonElement | null)[]>([])
  const approach = problem.approaches[selected]

  if (!approach) {
    return <p className="muted">No approaches have been written yet.</p>
  }

  function select(index: number) {
    const next = new URLSearchParams(searchParams)
    next.set('approach', problem.approaches[index].meta.id)
    setSearchParams(next, { replace: true })
  }

  function onKeyDown(event: KeyboardEvent<HTMLButtonElement>, index: number) {
    if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return
    event.preventDefault()
    const direction = event.key === 'ArrowRight' ? 1 : -1
    const nextIndex = (index + direction + problem.approaches.length) % problem.approaches.length
    select(nextIndex)
    tabs.current[nextIndex]?.focus()
  }

  return (
    <div className="solutions">
      <div className="tabs" role="tablist" aria-label="Approaches">
        {problem.approaches.map((item, index) => (
          <button
            key={item.meta.id}
            ref={(node) => {
              tabs.current[index] = node
            }}
            type="button"
            role="tab"
            id={`approach-tab-${item.meta.id}`}
            aria-selected={index === selected}
            aria-controls={`approach-panel-${item.meta.id}`}
            tabIndex={index === selected ? 0 : -1}
            className="tab"
            onClick={() => select(index)}
            onKeyDown={(event) => onKeyDown(event, index)}
          >
            {item.meta.name}
          </button>
        ))}
      </div>

      <div
        role="tabpanel"
        id={`approach-panel-${approach.meta.id}`}
        aria-labelledby={`approach-tab-${approach.meta.id}`}
        className="approach-panel"
      >
        <div className="complexity" aria-label="Complexity">
          <div>
            <span className="complexity-label">Time</span>
            <span className="complexity-value">{approach.meta.time}</span>
          </div>
          <div>
            <span className="complexity-label">Space</span>
            <span className="complexity-value">{approach.meta.space}</span>
          </div>
        </div>

        {approach.notes && <Markdown className="approach-notes">{approach.notes}</Markdown>}

        {selected === 0 ? (
          <Visualizer
            problemId={problem.meta.id}
            code={approach.code}
            filename={`${String(selected + 1).padStart(2, '0')}-${approach.meta.id}.py`}
          />
        ) : (
          <CodeBlock
            code={approach.code}
            label={`${String(selected + 1).padStart(2, '0')}-${approach.meta.id}.py`}
          />
        )}
      </div>
    </div>
  )
}
