import type { Difficulty as DifficultyName } from '../lib/content'

export function Difficulty({ value }: { value: DifficultyName }) {
  return (
    <span className={`difficulty difficulty-${value.toLowerCase()}`}>
      <span className="difficulty-dot" aria-hidden="true" />
      {value}
    </span>
  )
}
