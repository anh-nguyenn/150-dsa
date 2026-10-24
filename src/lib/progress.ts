import { useSyncExternalStore } from 'react'

export interface ProblemProgress {
  solved: boolean
  at: number
}

export interface ProgressState {
  version: 1
  lastProblem: string | null
  problems: Record<string, ProblemProgress>
}

const KEY = 'n150:progress'

function probeStorage(): boolean {
  try {
    const key = 'n150:probe'
    window.localStorage.setItem(key, '1')
    window.localStorage.removeItem(key)
    return true
  } catch {
    return false
  }
}

let storageAvailable = typeof window !== 'undefined' && probeStorage()

function initial(): ProgressState {
  return { version: 1, lastProblem: null, problems: {} }
}

function load(): ProgressState {
  if (!storageAvailable) return initial()
  try {
    const raw = window.localStorage.getItem(KEY)
    if (!raw) return initial()
    const parsed = JSON.parse(raw) as Partial<ProgressState>
    if (parsed.version !== 1 || typeof parsed.problems !== 'object' || parsed.problems === null) {
      return initial()
    }
    return {
      version: 1,
      lastProblem: typeof parsed.lastProblem === 'string' ? parsed.lastProblem : null,
      problems: parsed.problems,
    }
  } catch {
    return initial()
  }
}

let current = load()
const listeners = new Set<() => void>()

function emit() {
  listeners.forEach((listener) => listener())
}

function persist() {
  if (!storageAvailable) return
  try {
    window.localStorage.setItem(KEY, JSON.stringify(current))
  } catch {
    storageAvailable = false
    emit()
  }
}

export function subscribeProgress(listener: () => void): () => void {
  listeners.add(listener)
  return () => {
    listeners.delete(listener)
  }
}

export function getProgressSnapshot(): ProgressState {
  return current
}

export function isStorageAvailable(): boolean {
  return storageAvailable
}

export function toggleSolved(id: string) {
  const problems = { ...current.problems }
  if (problems[id]?.solved) {
    delete problems[id]
  } else {
    problems[id] = { solved: true, at: Date.now() }
  }
  current = { ...current, problems }
  persist()
  emit()
}

export function noteVisit(id: string) {
  if (current.lastProblem === id) return
  current = { ...current, lastProblem: id }
  persist()
  emit()
}

export function useProgress(): ProgressState {
  return useSyncExternalStore(subscribeProgress, getProgressSnapshot, getProgressSnapshot)
}

export function solvedCount(state: ProgressState): number {
  return Object.values(state.problems).filter((entry) => entry.solved).length
}
