import { useEffect, useMemo, useRef, useState } from 'react'
import { CodeBlock } from './CodeBlock'
import { highlightLine } from '../lib/highlight'
import { loadTrace, type TraceFile, type TraceValue } from '../lib/trace'



interface VisualizerProps {
  problemId: string
  code: string
  filename: string
}

function asArray(value: unknown): unknown[] {
  return Array.isArray(value) ? value : []
}

function asSummaries(value: unknown): TraceValue[] {
  return Array.isArray(value) ? (value as TraceValue[]) : []
}

function formatScalar(value: unknown): string {
  if (value === null || value === undefined) return 'null'
  if (typeof value === 'string') return value
  if (typeof value === 'boolean') return value ? 'true' : 'false'
  if (typeof value === 'number') return Number.isInteger(value) ? String(value) : String(value)
  return JSON.stringify(value)
}

function isTraceValue(value: unknown): value is TraceValue {
  return Boolean(value) && typeof value === 'object' && 'kind' in (value as Record<string, unknown>)
}

function formatItem(value: unknown): string {
  return isTraceValue(value) ? formatCompact(value) : formatScalar(value)
}

function truncate(text: string, limit = 46): string {
  return text.length <= limit ? text : text.slice(0, limit - 1) + '…'
}

function formatCompact(value: TraceValue): string {
  if (value.kind === 'scalar') return formatScalar(value.value)
  if (value.kind === 'string') {
    const text = String(value.value ?? '')
    return `"${truncate(text, 28)}"`
  }
  if (value.kind === 'array' || value.kind === 'queue' || value.kind === 'set') {
    const items = asArray(value.value)
    return truncate(`[${items.slice(0, 6).map(formatItem).join(', ')}${items.length > 6 ? ', …' : ''}]`, 44)
  }
  if (value.kind === 'grid') {
    const rows = asArray(value.value)
    const cols = rows[0] && Array.isArray(rows[0]) ? rows[0].length : 0
    return `${value.rows ?? rows.length}×${value.cols ?? cols} grid`
  }
  if (value.kind === 'map') {
    return `{${(value.entries ?? []).slice(0, 4).map((entry) => `${entry.key}: ${formatCompact(entry.value)}`).join(', ')}${(value.entries ?? []).length > 4 ? ', …' : ''}}`
  }
  if (value.kind === 'object') {
    return `{${value.class ?? 'object'}}`
  }
  if (value.kind === 'tree') {
    return `tree [${asArray(value.value).slice(0, 8).map(formatItem).join(', ')}]`
  }
  if (value.kind === 'linked_list') {
    return `list [${asArray(value.value).slice(0, 8).map(formatItem).join(' → ')}]`
  }
  if (value.kind === 'graph') {
    return `graph with ${asArray(value.value).length} nodes`
  }
  if (value.kind === 'random_list') {
    return 'random list'
  }
  if (value.kind === 'list') {
    return `[${asSummaries(value.value).slice(0, 4).map(formatCompact).join(', ')}]`
  }
  return truncate(String(value.value ?? ''), 44)
}

function signature(value: TraceValue): string {
  return JSON.stringify(value)
}

function treeLevels(value: unknown[]): unknown[][] {
  const levels: unknown[][] = []
  let start = 0
  let width = 1
  while (start < value.length && levels.length < 7) {
    levels.push(value.slice(start, start + width))
    start += width
    width *= 2
  }
  return levels
}

function ArrayView({ value, pointers }: { value: TraceValue; pointers: Map<number, string[]> }) {
  const items = asArray(value.value)
  if (items.length === 0) return <span className="viz-empty">empty</span>
  return (
    <div className="viz-row">
      {items.map((item, index) => (
        <div className="viz-cell-wrap" key={index}>
          {pointers.get(index)?.length ? (
            <span className="viz-pointer-stack">
              {pointers.get(index)?.map((pointer) => (
                <span className="viz-pointer" key={pointer}>
                  {pointer}
                </span>
              ))}
            </span>
          ) : (
            <span className="viz-pointer" />
          )}
          <span className="viz-cell">{formatScalar(item)}</span>
          <span className="viz-index">{index}</span>
        </div>
      ))}
      {value.truncated && <span className="viz-more">…{value.length ?? items.length}</span>}
    </div>
  )
}

function StringView({ value, pointers }: { value: TraceValue; pointers: Map<number, string[]> }) {
  const text = String(value.value ?? '')
  if (!text) return <span className="viz-empty">empty string</span>
  return (
    <div className="viz-row">
      {text.split('').map((char, index) => (
        <div className="viz-cell-wrap" key={index}>
          {pointers.get(index)?.length ? (
            <span className="viz-pointer-stack">
              {pointers.get(index)?.map((pointer) => (
                <span className="viz-pointer" key={pointer}>
                  {pointer}
                </span>
              ))}
            </span>
          ) : (
            <span className="viz-pointer" />
          )}
          <span className="viz-cell viz-char">{char === ' ' ? '·' : char}</span>
          <span className="viz-index">{index}</span>
        </div>
      ))}
      {value.truncated && <span className="viz-more">…</span>}
    </div>
  )
}

function GridView({ value, activeCell }: { value: TraceValue; activeCell?: [number, number] }) {
  const rows = asArray(value.value) as unknown[][]
  if (rows.length === 0) return <span className="viz-empty">empty grid</span>
  const width = Math.max(...rows.map((row) => (Array.isArray(row) ? row.length : 0)))
  return (
    <div className="viz-grid-scroll">
      <table className="viz-grid">
        <thead>
          <tr>
            <th aria-label="row" />
            {Array.from({ length: width }, (_, index) => (
              <th key={index}>{index}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              <th>{rowIndex}</th>
              {Array.from({ length: width }, (_, colIndex) => {
                const active = activeCell?.[0] === rowIndex && activeCell?.[1] === colIndex
                const content = Array.isArray(row) ? row[colIndex] : undefined
                return (
                  <td className={active ? 'is-active' : ''} key={colIndex}>
                    {content === undefined ? '' : formatScalar(content)}
                  </td>
                )
              })}
            </tr>
          ))}
        </tbody>
      </table>
      {value.truncated && <p className="viz-more">Showing the first cells of a {value.rows}×{value.cols} grid.</p>}
    </div>
  )
}

function MapView({ value }: { value: TraceValue }) {
  const entries = value.entries ?? []
  if (entries.length === 0) return <span className="viz-empty">empty map</span>
  return (
    <div className="viz-map">
      {entries.map((entry, index) => (
        <div className="viz-map-row" key={`${entry.key}-${index}`}>
          <span className="viz-map-key">{entry.key}</span>
          <span className="viz-map-arrow">→</span>
          <span className="viz-map-value">{formatCompact(entry.value)}</span>
        </div>
      ))}
      {value.truncated && <span className="viz-more">…{value.length ?? entries.length} entries</span>}
    </div>
  )
}

function SetView({ value }: { value: TraceValue }) {
  const items = asArray(value.value)
  if (items.length === 0) return <span className="viz-empty">empty set</span>
  return (
    <div className="viz-row viz-wrap">
      {items.map((item, index) => (
        <span className="viz-chip" key={index}>
          {formatItem(item)}
        </span>
      ))}
      {value.truncated && <span className="viz-more">…{value.length ?? items.length}</span>}
    </div>
  )
}

function TreeView({ value }: { value: TraceValue }) {
  const levels = treeLevels(asArray(value.value))
  if (levels.length === 0) return <span className="viz-empty">empty tree</span>
  return (
    <div className="viz-tree">
      {levels.map((level, index) => (
        <div className="viz-tree-level" key={index}>
          <span className="viz-tree-depth">{index}</span>
          <div className="viz-row viz-wrap">
            {level.map((node, nodeIndex) => (
              <span className={node === null ? 'viz-chip is-empty' : 'viz-chip'} key={nodeIndex}>
                {node === null ? '·' : formatScalar(node)}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

function LinkedListView({ value }: { value: TraceValue }) {
  const items = asArray(value.value)
  if (items.length === 0) return <span className="viz-empty">empty list</span>
  return (
    <div className="viz-row viz-wrap">
      {items.map((item, index) => (
        <span className="viz-list-node" key={index}>
          <span className="viz-chip">{formatScalar(item)}</span>
          {index < items.length - 1 && <span className="viz-link">→</span>}
        </span>
      ))}
      {value.truncated && <span className="viz-more">…</span>}
    </div>
  )
}

function GraphView({ value }: { value: TraceValue }) {
  const adjacency = asArray(value.value)
  if (adjacency.length === 0) return <span className="viz-empty">empty graph</span>
  return (
    <div className="viz-map">
      {adjacency.map((neighbors, index) => (
        <div className="viz-map-row" key={index}>
          <span className="viz-map-key">{index + 1}</span>
          <span className="viz-map-arrow">→</span>
          <span className="viz-map-value">{asArray(neighbors).join(', ') || '—'}</span>
        </div>
      ))}
    </div>
  )
}

function RandomListView({ value }: { value: TraceValue }) {
  const items = asArray(value.value)
  if (items.length === 0) return <span className="viz-empty">empty list</span>
  return (
    <div className="viz-map">
      {items.map((item, index) => {
        const pair = asArray(item)
        return (
          <div className="viz-map-row" key={index}>
            <span className="viz-map-key">{formatScalar(pair[0])}</span>
            <span className="viz-map-arrow">random</span>
            <span className="viz-map-value">{pair[1] === null ? 'null' : formatScalar(pair[1])}</span>
          </div>
        )
      })}
    </div>
  )
}

function ObjectView({ value }: { value: TraceValue }) {
  const attributes = value.attributes ?? []
  if (attributes.length === 0) return <span className="viz-empty">{value.class ?? 'object'}</span>
  return (
    <div className="viz-object">
      <span className="viz-object-class">{value.class}</span>
      {attributes.map((attribute, index) => (
        <div className="viz-object-row" key={`${attribute.name}-${index}`}>
          <span className="viz-map-key">{attribute.name}</span>
          <span className="viz-map-arrow">=</span>
          <span className="viz-map-value">{formatCompact(attribute)}</span>
        </div>
      ))}
    </div>
  )
}

function ValueView({
  value,
  pointers,
  activeCell,
}: {
  value: TraceValue
  pointers: Map<number, string[]>
  activeCell?: [number, number]
}) {
  if (value.kind === 'array') return <ArrayView value={value} pointers={pointers} />
  if (value.kind === 'string') return <StringView value={value} pointers={pointers} />
  if (value.kind === 'grid') return <GridView value={value} activeCell={activeCell} />
  if (value.kind === 'map') return <MapView value={value} />
  if (value.kind === 'set') return <SetView value={value} />
  if (value.kind === 'queue') return <SetView value={value} />
  if (value.kind === 'tree') return <TreeView value={value} />
  if (value.kind === 'linked_list') return <LinkedListView value={value} />
  if (value.kind === 'graph') return <GraphView value={value} />
  if (value.kind === 'random_list') return <RandomListView value={value} />
  if (value.kind === 'object') return <ObjectView value={value} />
  if (value.kind === 'list') {
    const items = asSummaries(value.value)
    if (items.length === 0) return <span className="viz-empty">empty list</span>
    return (
      <div className="viz-row viz-wrap">
        {items.map((item, index) => (
          <span className="viz-chip" key={index}>
            {formatCompact(item)}
          </span>
        ))}
      </div>
    )
  }
  if (value.kind === 'scalar') return <span className="viz-scalar">{formatScalar(value.value)}</span>
  return <span className="viz-text">{formatCompact(value)}</span>
}

function TraceCode({ code, activeLine, filename }: { code: string; activeLine: number; filename: string }) {
  const lines = useMemo(() => code.replace(/\r\n/g, '\n').replace(/\n$/, '').split('\n'), [code])
  const scroll = useRef<HTMLDivElement>(null)
  const active = useRef<HTMLDivElement>(null)
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    const container = scroll.current
    const line = active.current
    if (!container || !line) return
    const lineTop =
      line.getBoundingClientRect().top -
      container.getBoundingClientRect().top +
      container.scrollTop
    const top = lineTop - container.clientHeight / 2 + line.clientHeight / 2
    container.scrollTo({ top: Math.max(0, top), behavior: 'auto' })
  }, [activeLine])

  useEffect(() => {
    if (!copied) return
    const timer = window.setTimeout(() => setCopied(false), 1500)
    return () => window.clearTimeout(timer)
  }, [copied])

  async function copy() {
    try {
      await navigator.clipboard.writeText(code)
      setCopied(true)
    } catch {
      setCopied(false)
    }
  }

  return (
    <div className="trace-code">
      <div className="trace-code-head">
        <span>{filename}</span>
        <button type="button" className="code-copy" onClick={copy}>
          {copied ? 'Copied' : 'Copy'}
        </button>
      </div>
      <div className="trace-code-scroll" ref={scroll}>
        <pre className="trace-pre" aria-label="Reference solution code">
          {lines.map((line, index) => {
            const lineNumber = index + 1
            const isActive = lineNumber === activeLine
            return (
              <div className={isActive ? 'trace-line is-active' : 'trace-line'} key={index} ref={isActive ? active : null}>
                <span className="ln" aria-hidden="true">
                  {lineNumber}
                </span>
                <span className="lc">{highlightLine(line.replace(/\t/g, '    '), lineNumber)}</span>
              </div>
            )
          })}
        </pre>
      </div>
    </div>
  )
}



export function Visualizer({ problemId, code, filename }: VisualizerProps) {
  const [trace, setTrace] = useState<TraceFile | null>(null)
  const [loading, setLoading] = useState(true)
  const [index, setIndex] = useState(0)
  const [playing, setPlaying] = useState(false)
  const [speed, setSpeed] = useState(1)
  const player = useRef<HTMLDivElement>(null)

  useEffect(() => {
    let active = true
    setLoading(true)
    setTrace(null)
    setIndex(0)
    setPlaying(false)
    loadTrace(problemId)
      .then((loaded) => {
        if (!active) return
        setTrace(loaded ?? null)
        setLoading(false)
      })
      .catch(() => {
        if (!active) return
        setTrace(null)
        setLoading(false)
      })
    return () => {
      active = false
    }
  }, [problemId])

  const frames = trace?.frames ?? []
  const last = frames.length - 1
  const frame = frames[Math.min(index, last)]

  useEffect(() => {
    if (!playing || frames.length === 0) return
    const timer = window.setInterval(() => {
      setIndex((current) => Math.min(frames.length - 1, current + 1))
    }, 900 / speed)
    return () => window.clearInterval(timer)
  }, [playing, speed, frames.length])

  useEffect(() => {
    if (playing && index >= frames.length - 1) setPlaying(false)
  }, [playing, index, frames.length])

  if (loading) {
    return <div className="viz-panel viz-loading">Preparing visualization…</div>
  }

  if (!trace || !trace.ok || frames.length === 0 || !frame) {
    return (
      <div className="viz-panel">
        <p className="viz-fallback-note">
          A step-through trace is not available for this lesson yet. The reference code is below.
        </p>
        <CodeBlock code={code} label={filename} />
      </div>
    )
  }

  const previous = index > 0 ? frames[index - 1].vars : []
  const previousByName = new Map(previous.filter((item) => item.name).map((item) => [item.name, signature(item)]))
  const changed = new Set(
    frame.vars.filter((item) => item.name && previousByName.get(item.name) !== signature(item)).map((item) => item.name as string),
  )
  const scalarVars = frame.vars.filter((item) => item.kind === 'scalar')
  const panelVars = frame.vars.filter((item) => item.kind !== 'scalar')
  const gridPanels = frame.vars.filter((item) => item.kind === 'grid')
  const numericScalars = scalarVars.filter(
    (item): item is TraceValue & { name: string; value: number } =>
      typeof item.value === 'number' && typeof item.name === 'string',
  )
  const indexNames = trace.index_names ?? {}
  let activeCell: [number, number] | undefined
  if (gridPanels.length === 1) {
    const grid = gridPanels[0]
    const allowed = new Set(indexNames[grid.name ?? ''] ?? [])
    const byName = new Map(numericScalars.map((pointer) => [pointer.name, pointer.value]))
    let row: number | undefined
    let col: number | undefined
    for (const name of ['r', 'row', 'i', 'nr']) {
      if (allowed.has(name) && byName.has(name)) {
        row = byName.get(name)
        break
      }
    }
    for (const name of ['c', 'col', 'j', 'nc']) {
      if (allowed.has(name) && byName.has(name)) {
        col = byName.get(name)
        break
      }
    }
    if (row !== undefined && col !== undefined) activeCell = [row, col]
  }

  const codeLines = code.replace(/\r\n/g, '\n').split('\n')
  const sourceLine = (codeLines[frame.line - 1] ?? '').trim()
  const changedDetails = Array.from(changed)
    .filter((name) => name !== 'self')
    .slice(0, 4)
    .map((name) => {
      const variable = frame.vars.find((item) => item.name === name)
      return variable ? `${name} = ${formatCompact(variable)}` : name
    })

  function go(next: number) {
    setIndex(Math.max(0, Math.min(last, next)))
  }

  function step(direction: number) {
    setPlaying(false)
    go(index + direction)
  }

  function togglePlay() {
    if (playing) {
      setPlaying(false)
      return
    }
    if (index >= last) go(0)
    setPlaying(true)
  }

  function onKeyDown(event: React.KeyboardEvent<HTMLDivElement>) {
    const target = event.target as HTMLElement
    if (['INPUT', 'SELECT', 'TEXTAREA', 'BUTTON'].includes(target.tagName)) return
    if (event.key === 'ArrowLeft') {
      event.preventDefault()
      step(-1)
    } else if (event.key === 'ArrowRight') {
      event.preventDefault()
      step(1)
    } else if (event.key === 'Home') {
      event.preventDefault()
      setPlaying(false)
      go(0)
    } else if (event.key === 'End') {
      event.preventDefault()
      setPlaying(false)
      go(last)
    } else if (event.key === ' ') {
      event.preventDefault()
      togglePlay()
    }
  }

  return (
    <div
      className="viz-panel"
      ref={player}
      tabIndex={0}
      role="region"
      aria-label="Reference solution visualization"
      onKeyDown={onKeyDown}
      onClick={(event) => {
        const target = event.target as HTMLElement
        if (!target.closest('button, input, select, a')) player.current?.focus()
      }}
    >
      <div className="viz-head">
        <div className="viz-head-left">
          <span className="kicker">Watch</span>
          <span className="viz-case">{trace.case.name}</span>
          {trace.kind === 'class' && <span className="viz-tag">design</span>}
          {trace.truncated && <span className="viz-tag viz-tag-warn">trace truncated</span>}
        </div>
        <span className="viz-counter">
          {index + 1} / {frames.length}
        </span>
      </div>

      <div className="viz-body">
        <TraceCode code={code} activeLine={frame.line} filename={filename} />
        <div className="viz-state">
          <div className="viz-state-head">
            <span>State</span>
            <span>
              {frame.function}(){frame.depth > 0 ? ` · depth ${frame.depth}` : ''}
            </span>
          </div>
          <div className="viz-state-scroll">
            {scalarVars.length > 0 && (
              <div className="viz-scalars">
                {scalarVars.map((variable, variableIndex) => (
                  <span
                    className={changed.has(variable.name ?? '') ? 'viz-scalar-chip is-changed' : 'viz-scalar-chip'}
                    key={`${variable.name}-${variableIndex}`}
                  >
                    <span className="viz-scalar-name">{variable.name}</span>
                    <span className="viz-scalar-value">{formatScalar(variable.value)}</span>
                  </span>
                ))}
              </div>
            )}
            <div className="viz-vars">
              {panelVars.map((variable, variableIndex) => {
                const allowed = new Set(indexNames[variable.name ?? ''] ?? [])
                const pointers = new Map<number, string[]>()
                for (const pointer of numericScalars) {
                  if (!allowed.has(pointer.name) || pointer.value < 0) continue
                  const labels = pointers.get(pointer.value) ?? []
                  labels.push(pointer.name)
                  pointers.set(pointer.value, labels)
                }
                return (
                  <div
                    className={changed.has(variable.name ?? '') ? 'viz-var is-changed' : 'viz-var'}
                    key={`${variable.name}-${variableIndex}`}
                  >
                    <div className="viz-var-head">
                      <span className="viz-var-name">{variable.name}</span>
                      <span className="viz-var-kind">{variable.kind.replace('_', ' ')}</span>
                    </div>
                    <ValueView
                      value={variable}
                      pointers={pointers}
                      activeCell={gridPanels.length === 1 && variable.kind === 'grid' ? activeCell : undefined}
                    />
                  </div>
                )
              })}
            </div>
            {trace.output && index === last && !trace.truncated && (
              <div className="viz-output">
                <span>Returned</span>
                <code>{formatCompact(trace.output)}</code>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="viz-caption" aria-live={playing ? 'off' : 'polite'}>
        <div className="viz-caption-code">
          <span>line {frame.line}</span>
          <code>{sourceLine || '—'}</code>
        </div>
        <div className="viz-caption-change">
          {changedDetails.length > 0 ? `changed: ${changedDetails.join(' · ')}` : frame.function + '()'}
        </div>
      </div>

      <div className="viz-controls">
        <div className="viz-buttons">
          <button type="button" onClick={() => { setPlaying(false); go(0) }} aria-label="First frame">
            |←
          </button>
          <button type="button" onClick={() => step(-1)} aria-label="Previous frame" disabled={index === 0}>
            ←
          </button>
          <button type="button" className="viz-play" onClick={togglePlay} aria-label={playing ? 'Pause' : 'Play'}>
            {playing ? 'Pause' : 'Play'}
          </button>
          <button type="button" onClick={() => step(1)} aria-label="Next frame" disabled={index === last}>
            →
          </button>
          <button type="button" onClick={() => { setPlaying(false); go(last) }} aria-label="Last frame">
            →|
          </button>
        </div>
        <input
          className="viz-scrub"
          type="range"
          min={0}
          max={Math.max(0, last)}
          value={index}
          aria-label="Frame"
          onChange={(event) => {
            setPlaying(false)
            go(Number(event.target.value))
          }}
        />
        <label className="viz-speed">
          <span>Speed</span>
          <select
            value={speed}
            aria-label="Playback speed"
            onChange={(event) => setSpeed(Number(event.target.value))}
          >
            <option value={0.5}>0.5×</option>
            <option value={1}>1×</option>
            <option value={1.5}>1.5×</option>
            <option value={2}>2×</option>
          </select>
        </label>
      </div>
      <p className="viz-hint">Trace generated from the reference solution · ← → step · space play</p>
    </div>
  )
}
