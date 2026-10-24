import { useEffect, useRef, useState } from 'react'
import type { Problem } from '../lib/content'
import { clearCode, loadCode, saveCode } from '../lib/code'
import { isStorageAvailable } from '../lib/progress'
import { useRunner } from '../lib/runner'
import { PythonEditor } from './PythonEditor'

function formatValue(value: unknown): string {
  if (value === undefined) return 'undefined'
  return JSON.stringify(value, null, 2)
}

export function TryIt({ problem }: { problem: Problem }) {
  const starter = problem.starter ?? ''
  const [code, setCode] = useState(() => loadCode(problem.meta.id) ?? starter)
  const codeRef = useRef(code)
  const { status, result, error, run, cancel, reset } = useRunner()
  const busy = status === 'loading' || status === 'running'

  useEffect(() => {
    reset()
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

  function runTests() {
    if (!problem.tests || !problem.meta.entry) return
    run({
      meta: { entry: problem.meta.entry, kind: problem.meta.kind ?? 'function' },
      tests: problem.tests,
      code,
    })
  }

  function resetEditor() {
    if (!window.confirm('Reset to the starter code? Your current code for this problem will be removed.')) return
    setCode(starter)
    clearCode(problem.meta.id)
  }

  const passed = result ? result.cases.filter((item) => item.passed).length : 0
  const shortcut = typeof navigator !== 'undefined' && /Mac|iPhone|iPad/.test(navigator.platform) ? '⌘↵' : 'Ctrl↵'
  const totalMs = result ? result.cases.reduce((total, item) => total + (item.ms ?? 0), 0) : 0

  return (
    <div className="tryit">
      <div className="editor-card">
        <div className="editor-head">
          <span>solution.py</span>
          <div className="editor-actions">
            <span className="editor-save">{isStorageAvailable() ? 'Saved locally' : 'Session only'}</span>
            <button type="button" className="text-button" onClick={resetEditor}>
              Reset
            </button>
          </div>
        </div>
        <PythonEditor value={code} onChange={setCode} onRun={runTests} />
      </div>

      <div className="run-bar">
        <span className="run-meta">
          {problem.tests
            ? `${problem.tests.cases.length} cases · ${(problem.tests.compare ?? 'exact').replace('_', ' ')} comparison`
            : 'No tests'}
        </span>
        <div className="run-actions">
          {busy && (
            <button type="button" className="btn" onClick={cancel}>
              Cancel
            </button>
          )}
          <button type="button" className="btn btn-primary" disabled={busy || !problem.tests} onClick={runTests}>
            {status === 'loading' ? 'Loading Python…' : status === 'running' ? 'Running…' : 'Run tests'}
            {!busy && <span className="kbd">{shortcut}</span>}
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
            Running {problem.tests?.cases.length ?? 0} cases. A runaway loop is stopped after 5 seconds.
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
              <span className={result.ok ? 'results-pass' : 'results-fail'}>
                {result.ok ? 'All cases passed' : `${passed} of ${result.cases.length} cases passed`}
              </span>
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
