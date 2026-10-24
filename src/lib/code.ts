const KEY = 'n150:code'

let memory: Record<string, string> | null = null

function readAll(): Record<string, string> {
  if (memory) return memory
  try {
    const raw = window.localStorage.getItem(KEY)
    const parsed = raw ? (JSON.parse(raw) as unknown) : null
    if (parsed && typeof parsed === 'object' && !Array.isArray(parsed)) {
      memory = parsed as Record<string, string>
    } else {
      memory = {}
    }
  } catch {
    memory = {}
  }
  return memory
}

function persist() {
  if (!memory) return
  try {
    window.localStorage.setItem(KEY, JSON.stringify(memory))
  } catch {
    return
  }
}

export function loadCode(id: string): string | undefined {
  const value = readAll()[id]
  return typeof value === 'string' ? value : undefined
}

export function saveCode(id: string, code: string) {
  const all = readAll()
  all[id] = code
  persist()
}

export function clearCode(id: string) {
  const all = readAll()
  delete all[id]
  persist()
}
