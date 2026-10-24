export type TraceKind =
  | 'array'
  | 'string'
  | 'scalar'
  | 'grid'
  | 'map'
  | 'set'
  | 'queue'
  | 'tree'
  | 'linked_list'
  | 'graph'
  | 'random_list'
  | 'list'
  | 'object'
  | 'text'

export interface TraceValue {
  name?: string
  kind: TraceKind
  value?: unknown
  length?: number
  truncated?: boolean
  rows?: number
  cols?: number
  entries?: { key: string; value: TraceValue }[]
  attributes?: TraceValue[]
  class?: string
}

export interface TraceFrame {
  line: number
  function: string
  depth: number
  vars: TraceValue[]
}

export interface TraceCase {
  name: string
  args: unknown[]
  ops?: string[] | null
}

export interface TraceFile {
  version: number
  problem: string
  ok: boolean
  error: string | null
  kind: 'function' | 'class'
  case: TraceCase
  output?: TraceValue | null
  frames: TraceFrame[]
  truncated: boolean
  case_index: number
}

const traceFiles = import.meta.glob('../../content/traces/*.json', {
  import: 'default',
}) as Record<string, () => Promise<TraceFile>>

const cache = new Map<string, TraceFile>()

export async function loadTrace(problemId: string): Promise<TraceFile | undefined> {
  const cached = cache.get(problemId)
  if (cached) return cached
  const key = `../../content/traces/${problemId}.json`
  const loader = traceFiles[key]
  if (!loader) return undefined
  const trace = await loader()
  cache.set(problemId, trace)
  return trace
}
