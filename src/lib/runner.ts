import { useSyncExternalStore } from 'react'

export interface CaseResult {
  name: string
  passed: boolean
  expected?: unknown
  actual?: unknown
  error?: string
  ms?: number
  args?: unknown[]
  ops?: string[]
}

export interface RunResult {
  ok: boolean
  error: string | null
  cases: CaseResult[]
}

export type RunnerStatus = 'idle' | 'loading' | 'running' | 'success' | 'fail' | 'error' | 'timeout'

export interface RunnerSnapshot {
  status: RunnerStatus
  result: RunResult | null
  error: string | null
}

interface Payload {
  meta: unknown
  tests: unknown
  code: string
}

const TIMEOUT_MS = 5000

class PythonRunner {
  private worker: Worker | null = null
  private ready = false
  private pending: { id: number; payload: Payload } | null = null
  private timer: number | null = null
  private nextId = 0
  private snapshot: RunnerSnapshot = { status: 'idle', result: null, error: null }
  private listeners = new Set<() => void>()

  subscribe = (listener: () => void) => {
    this.listeners.add(listener)
    return () => {
      this.listeners.delete(listener)
    }
  }

  getSnapshot = () => this.snapshot

  private set(patch: Partial<RunnerSnapshot>) {
    this.snapshot = { ...this.snapshot, ...patch }
    this.listeners.forEach((listener) => listener())
  }

  private clearTimer() {
    if (this.timer !== null) {
      window.clearTimeout(this.timer)
      this.timer = null
    }
  }

  private stopWorker() {
    this.worker?.terminate()
    this.worker = null
    this.ready = false
    this.clearTimer()
  }

  private ensureWorker() {
    if (this.worker) return
    const worker = new Worker(new URL('../runner/runner.worker.ts', import.meta.url), { type: 'module' })
    worker.onmessage = (event: MessageEvent) => {
      const data = event.data as { type: string; id?: number; result?: RunResult; error?: string }
      if (data.type === 'ready') {
        this.ready = true
        const pending = this.pending
        if (pending) {
          this.pending = null
          this.send(pending.id, pending.payload)
        }
        return
      }
      if (data.type === 'load-error') {
        this.stopWorker()
        this.pending = null
        this.set({
          status: 'error',
          result: null,
          error: `The Python runtime could not load. ${data.error ?? ''}`.trim(),
        })
        return
      }
      if (data.type === 'result' && data.result) {
        this.clearTimer()
        this.set({
          status: data.result.ok ? 'success' : data.result.error ? 'error' : 'fail',
          result: data.result,
          error: data.result.error,
        })
        return
      }
      if (data.type === 'run-error') {
        this.clearTimer()
        this.set({ status: 'error', result: null, error: data.error ?? 'The runner failed.' })
      }
    }
    worker.onerror = (event) => {
      this.stopWorker()
      this.pending = null
      this.set({
        status: 'error',
        result: null,
        error: event.message || 'The Python worker crashed. It will restart on the next run.',
      })
    }
    this.worker = worker
    worker.postMessage({ type: 'init' })
  }

  private send(id: number, payload: Payload) {
    if (!this.worker) return
    this.set({ status: 'running', result: null, error: null })
    this.worker.postMessage({ type: 'run', id, ...payload })
    this.clearTimer()
    this.timer = window.setTimeout(() => {
      this.stopWorker()
      this.pending = null
      this.set({
        status: 'timeout',
        result: null,
        error: 'Time limit exceeded. The Python worker was stopped and will restart on the next run.',
      })
    }, TIMEOUT_MS)
  }

  run = (payload: Payload) => {
    if (this.snapshot.status === 'loading' || this.snapshot.status === 'running') return
    this.clearTimer()
    const id = ++this.nextId
    this.pending = { id, payload }
    this.set({ status: 'loading', result: null, error: null })
    this.ensureWorker()
    if (this.ready) {
      const pending = this.pending
      this.pending = null
      this.send(pending.id, pending.payload)
    }
  }

  cancel = () => {
    this.stopWorker()
    this.pending = null
    this.set({ status: 'idle', result: null, error: 'Run cancelled.' })
  }

  reset = () => {
    if (this.snapshot.status === 'loading' || this.snapshot.status === 'running') {
      this.stopWorker()
    }
    this.pending = null
    this.clearTimer()
    this.set({ status: 'idle', result: null, error: null })
  }
}

export const pythonRunner = new PythonRunner()

export function useRunner() {
  const snapshot = useSyncExternalStore(pythonRunner.subscribe, pythonRunner.getSnapshot, pythonRunner.getSnapshot)
  return {
    ...snapshot,
    run: pythonRunner.run,
    cancel: pythonRunner.cancel,
    reset: pythonRunner.reset,
  }
}
