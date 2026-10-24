interface ProgressBarProps {
  value: number
  max: number
  label: string
}

export function ProgressBar({ value, max, label }: ProgressBarProps) {
  const percent = max > 0 ? Math.min(100, (value / max) * 100) : 0
  return (
    <div
      className="progress-track"
      role="progressbar"
      aria-label={label}
      aria-valuemin={0}
      aria-valuemax={max}
      aria-valuenow={value}
    >
      <span className="progress-fill" style={{ width: `${percent}%` }} />
    </div>
  )
}
