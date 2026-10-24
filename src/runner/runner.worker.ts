import harnessSource from '../../tools/n150_harness.py?raw'

const PYODIDE_VERSION = '0.26.4'
const PYODIDE_BASE = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`

type Pyodide = {
  runPython: (code: string) => unknown
  globals: {
    get: (name: string) => {
      (meta: string, tests: string, code: string): string
      destroy?: () => void
    }
  }
}

let runtime: Promise<Pyodide> | null = null

function getRuntime(): Promise<Pyodide> {
  if (!runtime) {
    runtime = (async () => {
      const { loadPyodide } = await import(/* @vite-ignore */ `${PYODIDE_BASE}pyodide.mjs`)
      const pyodide = (await loadPyodide({ indexURL: PYODIDE_BASE })) as Pyodide
      pyodide.runPython(harnessSource)
      return pyodide
    })()
  }
  return runtime
}

self.onmessage = async (event: MessageEvent) => {
  const data = event.data as { type: string; id?: number; meta?: unknown; tests?: unknown; code?: string }
  if (data.type === 'init') {
    try {
      await getRuntime()
      self.postMessage({ type: 'ready' })
    } catch (error) {
      runtime = null
      self.postMessage({
        type: 'load-error',
        error: error instanceof Error ? error.message : String(error),
      })
    }
    return
  }

  if (data.type === 'run' && data.id !== undefined) {
    try {
      const pyodide = await getRuntime()
      const runner = pyodide.globals.get('run_payload')
      try {
        const raw = runner(JSON.stringify(data.meta), JSON.stringify(data.tests), data.code ?? '')
        self.postMessage({ type: 'result', id: data.id, result: JSON.parse(raw) })
      } finally {
        runner.destroy?.()
      }
    } catch (error) {
      self.postMessage({
        type: 'run-error',
        id: data.id,
        error: error instanceof Error ? error.message : String(error),
      })
    }
  }
}
