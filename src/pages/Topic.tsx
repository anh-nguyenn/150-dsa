import { Link, useParams } from 'react-router-dom'
import { Difficulty } from '../components/Difficulty'
import { Markdown } from '../components/Markdown'
import { ProgressBar } from '../components/ProgressBar'
import {
  countWritten,
  getProblemsForTopic,
  getTopic,
  getTopicMarkdown,
  topicCount,
  topics,
} from '../lib/content'
import { useProgress } from '../lib/progress'
import { useDocumentTitle } from '../lib/useDocumentTitle'
import { NotFound } from './NotFound'

export function Topic() {
  const { topicId } = useParams()
  const topic = topicId ? getTopic(topicId) : undefined
  useDocumentTitle(topic ? `${topic.name} · 150` : 'Not found · 150')
  const progress = useProgress()

  if (!topic) return <NotFound />

  const problems = getProblemsForTopic(topic.id)
  const written = countWritten(problems)
  const solved = problems.filter((problem) => progress.problems[problem.meta.id]?.solved).length
  const next = problems.find((problem) => problem.available && !progress.problems[problem.meta.id]?.solved)
  const intro = getTopicMarkdown(topic.id)

  return (
    <div className="page topic-page">
      <Link to="/" className="backlink">
        <span aria-hidden="true">←</span> Contents
      </Link>

      <header className="topic-header">
        <p className="kicker">
          Topic {String(topics.findIndex((item) => item.id === topic.id) + 1).padStart(2, '0')} / {topicCount}
        </p>
        <h1>{topic.name}</h1>
        <p className="topic-lede">{topic.tagline}</p>
      </header>

      {intro && <Markdown className="topic-intro">{intro.replace(/^# .+\n+/, '')}</Markdown>}

      <section className="topic-progress" aria-labelledby="topic-progress-title">
        <div className="topic-progress-head">
          <p className="kicker" id="topic-progress-title">
            Progress
          </p>
          <p>
            {solved} of {problems.length} solved
            {written < problems.length && <span className="muted"> · {written} written</span>}
          </p>
        </div>
        <ProgressBar value={solved} max={problems.length} label={`${topic.name} solved`} />
      </section>

      {next && (
        <div className="topic-next">
          <span className="kicker">Next in this topic</span>
          <Link to={`/problem/${next.meta.id}`} className="topic-next-link">
            {next.meta.title} <span aria-hidden="true">→</span>
          </Link>
        </div>
      )}

      <section className="problem-table" aria-labelledby="problem-list-title">
        <div className="problem-table-head">
          <p className="kicker" id="problem-list-title">
            Problems
          </p>
          <p className="contents-hint">Study order</p>
        </div>
        <ol className="problem-list">
          {problems.map((problem, index) => {
            const isSolved = Boolean(progress.problems[problem.meta.id]?.solved)
            const content = (
              <>
                <span className="problem-index">{String(index + 1).padStart(2, '0')}</span>
                <span className="problem-title">{problem.meta.title}</span>
                <Difficulty value={problem.meta.difficulty} />
                <span className="problem-state">
                  {problem.available ? (
                    isSolved ? (
                      <span className="state-solved">Solved</span>
                    ) : (
                      <span>Open</span>
                    )
                  ) : (
                    <span className="status-muted">Not written</span>
                  )}
                </span>
                <span className="problem-arrow" aria-hidden="true">
                  {problem.available ? '→' : ''}
                </span>
              </>
            )
            return (
              <li key={problem.meta.id}>
                {problem.available ? (
                  <Link className={isSolved ? 'problem-row is-solved' : 'problem-row'} to={`/problem/${problem.meta.id}`}>
                    {content}
                  </Link>
                ) : (
                  <div className="problem-row is-unavailable">{content}</div>
                )}
              </li>
            )
          })}
        </ol>
      </section>
    </div>
  )
}
