import catalogJson from '../../content/catalog.json'

export type Difficulty = 'Easy' | 'Medium' | 'Hard'

export interface CatalogTopic {
  id: string
  name: string
  tagline: string
  problems: string[]
}

export interface Catalog {
  version: number
  topics: CatalogTopic[]
}

export interface ApproachMeta {
  id: string
  name: string
  time: string
  space: string
}

export interface Example {
  input?: string
  output?: string
  explanation?: string
  body?: string
}

export interface ProblemMeta {
  id: string
  title: string
  slug: string
  difficulty: Difficulty
  entry?: string
  kind?: 'function' | 'class'
  approaches: ApproachMeta[]
  examples?: Example[]
  constraints?: string[]
}

export interface TestCase {
  name: string
  args?: unknown[]
  expected?: unknown
  ops?: string[]
  adapters?: (string | null)[]
}

export interface TestsFile {
  kind?: 'function' | 'class'
  compare?: 'exact' | 'unordered' | 'unordered_deep' | 'float'
  tolerance?: number
  cases: TestCase[]
}

export interface LoadedApproach {
  meta: ApproachMeta
  code: string
  notes: string
}

export interface Problem {
  meta: ProblemMeta
  topicId: string
  topicName: string
  topicIndex: number
  order: number
  summary?: string
  background?: string
  hints?: string
  starter?: string
  tests?: TestsFile
  approaches: LoadedApproach[]
  examples: Example[]
  constraints: string[]
  available: boolean
}

const catalog = catalogJson as Catalog

const problemFiles = import.meta.glob('../../content/problems/**/*', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>

const topicFiles = import.meta.glob('../../content/topics/*.md', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>

function relativeKey(key: string, marker: string): string {
  const index = key.indexOf(marker)
  return index === -1 ? key : key.slice(index + marker.length)
}

const files = new Map<string, Map<string, string>>()

for (const [key, value] of Object.entries(problemFiles)) {
  const relative = relativeKey(key, 'content/problems/')
  const slash = relative.indexOf('/')
  if (slash === -1) continue
  const id = relative.slice(0, slash)
  const path = relative.slice(slash + 1)
  if (!files.has(id)) files.set(id, new Map())
  files.get(id)?.set(path, value)
}

const topicMarkdown = new Map<string, string>()
for (const [key, value] of Object.entries(topicFiles)) {
  const relative = relativeKey(key, 'content/topics/')
  topicMarkdown.set(relative.replace(/\.md$/, ''), value)
}

function readMeta(id: string): ProblemMeta | undefined {
  const raw = files.get(id)?.get('meta.json')
  if (!raw) return undefined
  try {
    return JSON.parse(raw) as ProblemMeta
  } catch {
    return undefined
  }
}

function readTests(id: string): TestsFile | undefined {
  const raw = files.get(id)?.get('tests.json')
  if (!raw) return undefined
  try {
    return JSON.parse(raw) as TestsFile
  } catch {
    return undefined
  }
}

const allProblems: Problem[] = []
const problemById = new Map<string, Problem>()
const topicById = new Map<string, CatalogTopic>()
const topicProblems = new Map<string, Problem[]>()

catalog.topics.forEach((topic, topicIndex) => {
  topicById.set(topic.id, topic)
  const list: Problem[] = []
  topic.problems.forEach((id, order) => {
    const problemFilesForId = files.get(id)
    const meta = readMeta(id)
    if (!problemFilesForId || !meta) return
    const approaches: LoadedApproach[] = (meta.approaches ?? []).map((approach, index) => {
      const stem = `approaches/${String(index + 1).padStart(2, '0')}-${approach.id}`
      return {
        meta: approach,
        code: problemFilesForId.get(`${stem}.py`) ?? '',
        notes: problemFilesForId.get(`${stem}.md`) ?? '',
      }
    })
    const summary = problemFilesForId.get('summary.md')
    const background = problemFilesForId.get('background.md')
    const hints = problemFilesForId.get('hints.md')
    const starter = problemFilesForId.get('starter.py')
    const tests = readTests(id)
    const available = Boolean(
      summary &&
        background &&
        hints &&
        starter &&
        tests &&
        approaches.length > 0 &&
        approaches.every((approach) => approach.code && approach.notes),
    )
    const problem: Problem = {
      meta,
      topicId: topic.id,
      topicName: topic.name,
      topicIndex,
      order,
      summary,
      background,
      hints,
      starter,
      tests,
      approaches,
      examples: meta.examples ?? [],
      constraints: meta.constraints ?? [],
      available,
    }
    list.push(problem)
    allProblems.push(problem)
    problemById.set(id, problem)
  })
  topicProblems.set(topic.id, list)
})

export const topics = catalog.topics
export const problems = allProblems
export const topicCount = catalog.topics.length

export function getTopic(id: string): CatalogTopic | undefined {
  return topicById.get(id)
}

export function getTopicMarkdown(id: string): string | undefined {
  return topicMarkdown.get(id)
}

export function getProblemsForTopic(id: string): Problem[] {
  return topicProblems.get(id) ?? []
}

export function getProblem(id: string): Problem | undefined {
  return problemById.get(id)
}

export function getNextProblem(solved: Record<string, { solved: boolean }>): Problem | undefined {
  return allProblems.find((problem) => problem.available && !solved[problem.meta.id]?.solved)
}

export function getPreviousAndNext(id: string): { previous?: Problem; next?: Problem } {
  const available = allProblems.filter((problem) => problem.available)
  const index = available.findIndex((problem) => problem.meta.id === id)
  return {
    previous: index > 0 ? available[index - 1] : undefined,
    next: index >= 0 && index < available.length - 1 ? available[index + 1] : undefined,
  }
}

export function countWritten(problemsToCount: Problem[] = allProblems): number {
  return problemsToCount.filter((problem) => problem.available).length
}
