import { useEffect, useRef, useState } from 'react'
import type { Problem, TestCase } from '../lib/content'
import { clearCode, loadCode, saveCode } from '../lib/code'
import { isStorageAvailable, toggleSolved, useProgress } from '../lib/progress'
import { useRunner } from '../lib/runner'
import { PythonEditor } from './PythonEditor'

function formatValue(value: unknown): string {
  if (value === undefined) return 'undefined'
  return JSON.stringify(value, null, 2)
}

function spacedJson(value: unknown): string {
  const text = JSON.stringify(value)
  let result = ''
  let inString = false
  let escaped = false
  for (const char of text) {
    if (escaped) {
      result += char
      escaped = false
      continue
    }
    if (inString && char === '\\') {
      result += char
      escaped = true
      continue
    }
    if (char === '"') {
      inString = !inString
      result += char
      continue
    }
    if (char === ',' && !inString) {
      result += ', '
      continue
    }
    result += char
  }
  return result
}

function formatArg(arg: unknown): string {
  if (arg && typeof arg === 'object' && !Array.isArray(arg)) {
    const wrapper = arg as Record<string, unknown>
    if ('tree' in wrapper) return `tree = ${spacedJson(wrapper.tree)}`
    if ('linked_list' in wrapper) return `list = ${spacedJson(wrapper.linked_list)}`
    if ('graph_adj' in wrapper) return `adjacency = ${spacedJson(wrapper.graph_adj)}`
    if ('random_list' in wrapper) return `nodes = ${spacedJson(wrapper.random_list)}`
  }
  return spacedJson(arg)
}

function splitParams(text: string): string[] {
  const parts: string[] = []
  let current = ''
  let depth = 0
  for (const char of text) {
    if ('([{<'.includes(char)) depth += 1
    if (')]}>'.includes(char)) depth -= 1
    if (char === ',' && depth === 0) {
      parts.push(current)
      current = ''
    } else {
      current += char
    }
  }
  if (current.trim()) parts.push(current)
  return parts
}

function parameterNames(starter: string, entry?: string): string[] {
  if (!entry) return []
  const escaped = entry.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  const match = starter.match(new RegExp(`def\\s+${escaped}\\s*\\(([^)]*)\\)`))
  if (!match) return []
  return splitParams(match[1]).map((part) => part.trim().split(':')[0].split('=')[0].trim())
}

function formatNamedArg(arg: unknown, name: string): string {
  if (arg && typeof arg === 'object' && !Array.isArray(arg)) {
    const wrapper = arg as Record<string, unknown>
    if ('tree' in wrapper) return `${name} = ${spacedJson(wrapper.tree)}`
    if ('linked_list' in wrapper) {
      const cycle = wrapper.cycle
      const suffix = cycle !== undefined && cycle !== null ? `, cycle = ${cycle}` : ''
      return `${name} = ${spacedJson(wrapper.linked_list)}${suffix}`
    }
    if ('graph_adj' in wrapper) return `${name} = ${spacedJson(wrapper.graph_adj)}`
    if ('random_list' in wrapper) return `${name} = ${spacedJson(wrapper.random_list)}`
  }
  return `${name} = ${spacedJson(arg)}`
}

function caseInput(test: TestCase | undefined, params: string[]): string {
  if (!test) return ''
  if (test.ops) {
    return test.ops
      .map((op, index) => {
        const raw = test.args?.[index]
        const args = Array.isArray(raw) ? raw : []
        return `${op}(${args.map(formatArg).join(', ')})`
      })
      .join('\n')
  }
  return (test.args ?? [])
    .map((arg, index) => (params[index] ? formatNamedArg(arg, params[index]) : formatArg(arg)))
    .join(', ')
}

export function TryIt({ problem }: { problem: Problem }) {
  const starter = problem.starter ?? ''
  const [code, setCode] = useState(() => loadCode(problem.meta.id) ?? starter)
  const [selectedCase, setSelectedCase] = useState(0)
  const [mode, setMode] = useState<'run' | 'submit' | null>(null)
  const codeRef = useRef(code)
  const progress = useProgress()
  const solved = Boolean(progress.problems[problem.meta.id]?.solved)
  const { status, result, error, run, cancel, reset } = useRunner()
  const busy = status === 'loading' || status === 'running'
  const cases = problem.tests?.cases ?? []
  const currentCase = cases[Math.min(selectedCase, Math.max(0, cases.length - 1))]
  const totalCases = cases.length
  const params = parameterNames(problem.starter ?? '', problem.meta.entry)

  useEffect(() => {
    reset()
    setSelectedCase(0)
    setMode(null)
    return () => reset()
  }, [problem.meta.id, reset])

  useEffect(() => {
    setCode(loadCode(problem.meta.id) ?? starter)
  }, [problem.meta.id, starter])

  useEffect(() => {
    codeRef.current = code
    const timer = window.setTimeout(() => saveCode(problem.meta.id, code), 350)
    return () => window.clearTimeout(timer)
  }, [problem.meta.id, code])

  useEffect(() => {
    const id = problem.meta.id
    return () => {
      saveCode(id, codeRef.current)
    }
  }, [problem.meta.id])

  useEffect(() => {
    if (mode === 'submit' && result?.ok && result.cases.length === totalCases && totalCases > 0 && !solved) {
      toggleSolved(problem.meta.id)
    }
  }, [mode, result, solved, totalCases, problem.meta.id])

  function runCase(index: number) {
    if (!problem.tests || !problem.meta.entry) return
    setMode('run')
    run({
      meta: { entry: problem.meta.entry, kind: problem.meta.kind ?? 'function' },
      tests: problem.tests,
      code,
      caseIndex: index,
    })
  }

  function submitAll() {
    if (!problem.tests || !problem.meta.entry) return
    setMode('submit')
    run({
      meta: { entry: problem.meta.entry, kind: problem.meta.kind ?? 'function' },
      tests: problem.tests,
      code,
    })
  }

  function selectCase(index: number) {
    if (busy || index === selectedCase) return
    reset()
    setMode(null)
    setSelectedCase(index)
  }

  function resetEditor() {
    if (!window.confirm('Reset to the starter code? Your current code for this problem will be removed.')) return
    setCode(starter)
    clearCode(problem.meta.id)
  }

  const passed = result ? result.cases.filter((item) => item.passed).length : 0
  const shortcut = typeof navigator !== 'undefined' && /Mac|iPhone|iPad/.test(navigator.platform) ? '⌘↵' : 'Ctrl↵'
  const totalMs = result ? result.cases.reduce((total, item) => total + (item.ms ?? 0), 0) : 0
  const runLabel = mode === 'submit' ? `Running ${totalCases} cases…` : `Running case ${selectedCase + 1}…`
  const resultLabel = (() => {
    if (!result) return ''
    if (mode === 'submit' || result.cases.length > 1) {
      return result.ok ? 'All cases passed' : `${passed} of ${result.cases.length} cases passed`
    }
    return result.ok ? 'Case passed' : 'Case failed'
  })()

  return (
    <div className="tryit">
      <div className="editor-card">
        <div className="editor-head">
          <span className="editor-lang">solution.py</span>
          <div className="editor-actions">
            <span className="editor-save">{isStorageAvailable() ? 'Saved locally' : 'Session only'}</span>
            <button type="button" className="text-button" onClick={resetEditor}>
              Reset
            </button>
          </div>
        </div>
        <PythonEditor value={code} onChange={setCode} onRun={() => runCase(selectedCase)} />
      </div>

      <div className="testcase-tabs" role="tablist" aria-label="Testcases">
        {cases.map((test, index) => (
          <button
            key={`${test.name}-${index}`}
            type="button"
            role="tab"
            aria-selected={index === selectedCase}
            aria-controls="testcase-panel"
            className="testcase-tab"
            title={test.name}
            disabled={busy}
            onClick={() => selectCase(index)}
          >
            Case {index + 1}
          </button>
        ))}
      </div>
      <div className="testcase-panel" id="testcase-panel" role="tabpanel" aria-label={`Case ${selectedCase + 1}`}>
        <div className="testcase-head">
          <span>{currentCase?.name ?? 'Testcase'}</span>
          <span>Authored · read only</span>
        </div>
        <pre className="testcase-input">{caseInput(currentCase, params)}</pre>
      </div>

      <div className="run-bar">
        <span className="run-meta">
          {problem.tests
            ? `${totalCases} cases · ${(problem.tests.compare ?? 'exact').replace('_', ' ')} comparison`
            : 'No tests'}
        </span>
        <div className="run-actions">
          {busy && (
            <button type="button" className="btn" onClick={cancel}>
              Cancel
            </button>
          )}
          <button
            type="button"
            className="btn"
            disabled={busy || totalCases === 0}
            onClick={() => runCase(selectedCase)}
          >
            Run {!busy && <span className="kbd">{shortcut}</span>}
          </button>
          <button type="button" className="btn btn-primary" disabled={busy || totalCases === 0} onClick={submitAll}>
            Submit
          </button>
        </div>
      </div>

      <div className="runner-area" aria-live="polite">
        {status === 'loading' && (
          <div className="runner-status">
            <span className="runner-pulse" aria-hidden="true" />
            Downloading the Python runtime once. This can take a few seconds.
          </div>
        )}
        {status === 'running' && (
          <div className="runner-status">
            <span className="runner-pulse" aria-hidden="true" />
            {runLabel} A runaway loop is stopped after 5 seconds.
          </div>
        )}
        {status === 'idle' && error && <div className="runner-message">{error}</div>}
        {status === 'timeout' && <div className="runner-error">{error}</div>}
        {status === 'error' && (
          <div className="runner-error">
            <p>{result && result.cases.length > 0 ? 'Some cases could not be evaluated.' : 'The code could not run.'}</p>
            {error && <pre>{error}</pre>}
          </div>
        )}
        {result && result.cases.length > 0 && (
          <div className="results">
            <div className="results-head">
              <span className={result.ok ? 'results-pass' : 'results-fail'}>{resultLabel}</span>
              <span className="results-meta">
                {totalMs < 0.1 ? '<0.1 ms total' : `${totalMs.toFixed(1)} ms total`}
              </span>
            </div>
            <ol className="result-list">
              {result.cases.map((item, index) => (
                <li className={item.passed ? 'result is-pass' : 'result is-fail'} key={`${item.name}-${index}`}>
                  <div className="result-row">
                    <span className="result-name">{item.name}</span>
                    <span className="result-state">{item.passed ? 'Pass' : 'Fail'}</span>
                    <span className="result-ms">
                      {item.ms === undefined ? '—' : item.ms < 0.1 ? '<0.1 ms' : `${item.ms.toFixed(1)} ms`}
                    </span>
                  </div>
                  {!item.passed && (
                    <div className="result-detail">
                      {item.error ? (
                        <div className="result-block">
                          <span>Error</span>
                          <pre>{item.error}</pre>
                        </div>
                      ) : (
                        <>
                          {(item.args || item.ops) && (
                            <div className="result-block">
                              <span>Input</span>
                              <pre>{formatValue(item.ops ?? item.args)}</pre>
                            </div>
                          )}
                          <div className="result-block">
                            <span>Expected</span>
                            <pre>{formatValue(item.expected)}</pre>
                          </div>
                          <div className="result-block">
                            <span>Actual</span>
                            <pre>{formatValue(item.actual)}</pre>
                          </div>
                        </>
                      )}
                    </div>
                  )}
                </li>
              ))}
            </ol>
          </div>
        )}
        {status === 'success' && result && result.cases.length === 0 && (
          <div className="runner-message">No cases were defined.</div>
        )}
      </div>

      <p className="tryit-note">
        Python runs locally in a Web Worker. The runtime is downloaded once and cached by the browser; code never leaves
        this device.
      </p>
    </div>
  )
}
