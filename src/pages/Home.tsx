import { Link } from 'react-router-dom'
import { ProgressBar } from '../components/ProgressBar'
import {
  countWritten,
  getProblemsForTopic,
  problems,
  topics,
} from '../lib/content'
import { solvedCount, useProgress } from '../lib/progress'
import { useDocumentTitle } from '../lib/useDocumentTitle'

export function Home() {
  useDocumentTitle('150 — Algorithm Study')
  const progress = useProgress()
  const solved = solvedCount(progress)
  const written = countWritten()
  const startedTopics = topics.filter((topic) => getProblemsForTopic(topic.id).some((problem) => problem.available)).length

  return (
    <div className="page home">
      <section className="progress-block" aria-labelledby="progress-title">
        <div className="progress-head">
          <p className="kicker" id="progress-title">
            Overall
          </p>
          <p className="progress-number">
            <strong>{solved}</strong>
            <span aria-hidden="true"> / </span>
            {problems.length}
          </p>
        </div>
        <ProgressBar value={solved} max={problems.length} label="Problems solved" />
        <div className="progress-notes">
          <span>
            {written} of {problems.length} lessons written
          </span>
          <span>
            {startedTopics} of {topics.length} topics started
          </span>
          {problems.length - written > 0 && <span>{problems.length - written} lessons in progress</span>}
        </div>
      </section>

      <section className="contents" aria-labelledby="contents-title">
        <div className="contents-head">
          <p className="kicker" id="contents-title">
            Contents
          </p>
          <p className="contents-hint">18 topics, in study order</p>
        </div>
        <ol className="topic-list">
          {topics.map((topic, index) => {
            const topicProblems = getProblemsForTopic(topic.id)
            const topicSolved = topicProblems.filter((problem) => progress.problems[problem.meta.id]?.solved).length
            const topicWritten = countWritten(topicProblems)
            const planned = topicWritten === 0
            return (
              <li key={topic.id}>
                <Link className={planned ? 'topic-row is-planned' : 'topic-row'} to={`/topic/${topic.id}`}>
                  <span className="topic-index">{String(index + 1).padStart(2, '0')}</span>
                  <span className="topic-name-group">
                    <span className="topic-name">{topic.name}</span>
                    <span className="topic-tagline">{topic.tagline}</span>
                  </span>
                  <span className="topic-status">
                    {planned ? (
                      <span className="status-muted">Planned</span>
                    ) : (
                      <>
                        <span className={topicSolved > 0 ? 'status-solved' : ''}>
                          {topicSolved} / {topicProblems.length} solved
                        </span>
                        {topicWritten < topicProblems.length && (
                          <span className="status-muted">{topicWritten} written</span>
                        )}
                      </>
                    )}
                  </span>
                  <span className="topic-arrow" aria-hidden="true">
                    →
                  </span>
                </Link>
              </li>
            )
          })}
        </ol>
      </section>
    </div>
  )
}
