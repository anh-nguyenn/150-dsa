import { lazy, Suspense, useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { Difficulty } from '../components/Difficulty'
import { Hints } from '../components/Hints'
import { Markdown } from '../components/Markdown'
import { Solutions } from '../components/Solutions'
import {
  getPreviousAndNext,
  getProblem,
  getProblemsForTopic,
  type Problem as ProblemData,
} from '../lib/content'
import { noteVisit, toggleSolved, useProgress } from '../lib/progress'
import { useDocumentTitle } from '../lib/useDocumentTitle'
import { NotFound } from './NotFound'

const TryIt = lazy(() => import('../components/TryIt').then((module) => ({ default: module.TryIt })))

const SECTIONS = [
  { id: 'summary', label: 'Summary' },
  { id: 'background', label: 'Background' },
  { id: 'hints', label: 'Hints' },
  { id: 'solutions', label: 'Solutions' },
  { id: 'try-it', label: 'Try it' },
]

export function Problem() {
  const { problemId } = useParams()
  const problem = problemId ? getProblem(problemId) : undefined
  useDocumentTitle(problem ? `${problem.meta.title} · 150` : 'Not found · 150')

  useEffect(() => {
    if (problem?.available) noteVisit(problem.meta.id)
  }, [problem])

  if (!problem) return <NotFound />
  if (!problem.available) return <PlannedLesson problem={problem} />
  return <Lesson problem={problem} />
}

function PlannedLesson({ problem }: { problem: ProblemData }) {
  return (
    <div className="page planned-lesson">
      <Link to={`/topic/${problem.topicId}`} className="backlink">
        <span aria-hidden="true">←</span> {problem.topicName}
      </Link>
      <p className="kicker">Lesson in progress</p>
      <h1>{problem.meta.title}</h1>
      <div className="planned-meta">
        <Difficulty value={problem.meta.difficulty} />
        <span className="status-muted">Not written yet</span>
      </div>
      <p className="planned-copy">
        This problem is in the catalog, but its lesson has not been written and verified yet. The page will appear here
        when it is ready; no half-built lesson is shown.
      </p>
      <Link className="btn btn-primary" to={`/topic/${problem.topicId}`}>
        Back to {problem.topicName} <span aria-hidden="true">→</span>
      </Link>
    </div>
  )
}

function Lesson({ problem }: { problem: ProblemData }) {
  const progress = useProgress()
  const solved = Boolean(progress.problems[problem.meta.id]?.solved)
  const { previous, next } = getPreviousAndNext(problem.meta.id)
  const [active, setActive] = useState('summary')
  const [mobileView, setMobileView] = useState<'read' | 'solutions' | 'try'>('read')

  useEffect(() => {
    setActive('summary')
    setMobileView('read')
  }, [problem.meta.id])

  useEffect(() => {
    let frame = 0
    const update = () => {
      frame = 0
      const offset = 130
      let current = SECTIONS[0].id
      for (const section of SECTIONS) {
        const element = document.getElementById(section.id)
        if (element && element.getBoundingClientRect().top <= offset) current = section.id
      }
      const atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2
      if (atBottom) current = SECTIONS[SECTIONS.length - 1].id
      setActive(current)
    }
    const onScroll = () => {
      if (frame) return
      frame = window.requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
      if (frame) window.cancelAnimationFrame(frame)
    }
  }, [problem.meta.id])

  return (
    <div className="problem-page" data-mobile-view={mobileView}>
      <div className="problem-bar">
        <div className="problem-bar-inner">
          <Link to={`/topic/${problem.topicId}`} className="problem-back">
            <span aria-hidden="true">←</span> <span className="problem-back-text">{problem.topicName}</span>
            <span className="problem-back-short">Topic</span>
          </Link>
          <span className="problem-bar-title">{problem.meta.title}</span>
          <Difficulty value={problem.meta.difficulty} />
          <span className="spacer" />
          <nav className="problem-nav" aria-label="Problem navigation">
            {previous && (
              <Link to={`/problem/${previous.meta.id}`} className="problem-nav-link" title={previous.meta.title}>
                <span aria-hidden="true">←</span> Prev
              </Link>
            )}
            {next && (
              <Link to={`/problem/${next.meta.id}`} className="problem-nav-link" title={next.meta.title}>
                Next <span aria-hidden="true">→</span>
              </Link>
            )}
          </nav>
          <button
            type="button"
            className="solved-toggle"
            aria-pressed={solved}
            onClick={() => {
              toggleSolved(problem.meta.id)
            }}
          >
            <span className="check" aria-hidden="true">
              {solved ? '✓' : ''}
            </span>
            {solved ? 'Solved' : 'Mark solved'}
          </button>
        </div>
      </div>

      <div className="mobile-switch" role="group" aria-label="Problem view">
        {(
          [
            ['read', 'Read'],
            ['solutions', 'Solutions'],
            ['try', 'Try it'],
          ] as const
        ).map(([value, label]) => (
          <button
            key={value}
            type="button"
            aria-pressed={mobileView === value}
            onClick={() => setMobileView(value)}
          >
            {label}
          </button>
        ))}
      </div>

      <div className="problem-layout">
        <div className="problem-main">
          <header className="problem-header">
            <p className="kicker">
              {problem.topicName} <span aria-hidden="true">·</span> problem {problem.order + 1} of{' '}
              {getProblemsForTopic(problem.topicId).length}
            </p>
            <h1>{problem.meta.title}</h1>
            <div className="problem-header-meta">
              <Difficulty value={problem.meta.difficulty} />
              <span>{problem.approaches.length} approach</span>
              <span>{problem.tests?.cases.length ?? 0} tests</span>
            </div>
          </header>

          <div className="group group-read">
            <section className="section" id="summary" aria-labelledby="summary-title">
              <SectionHead index="01" id="summary-title" title="Summary" />
              {problem.summary && <Markdown>{problem.summary}</Markdown>}
            </section>

            <section className="section" id="background" aria-labelledby="background-title">
              <SectionHead index="02" id="background-title" title="Background" />
              {problem.background && <Markdown>{problem.background}</Markdown>}
            </section>

            <section className="section" id="hints" aria-labelledby="hints-title">
              <SectionHead index="03" id="hints-title" title="Hints" />
              {problem.hints && <Hints markdown={problem.hints} />}
            </section>
          </div>

          <div className="group group-solutions">
            <section className="section" id="solutions" aria-labelledby="solutions-title">
              <SectionHead index="04" id="solutions-title" title="Solutions" />
              <Solutions problem={problem} />
            </section>
          </div>

          <div className="group group-try">
            <section className="section" id="try-it" aria-labelledby="try-it-title">
              <SectionHead index="05" id="try-it-title" title="Try it" />
              {problem.starter && (
                <Suspense fallback={<div className="editor-loading">Loading editor…</div>}>
                  <TryIt key={problem.meta.id} problem={problem} />
                </Suspense>
              )}
            </section>
          </div>

          <div className="lesson-end">
            <button
              type="button"
              className="solved-toggle solved-toggle-large"
              aria-pressed={solved}
              onClick={() => {
                toggleSolved(problem.meta.id)
              }}
            >
              <span className="check" aria-hidden="true">
                {solved ? '✓' : ''}
              </span>
              {solved ? 'Solved' : 'Mark solved'}
            </button>
            {next ? (
              <Link className="text-link" to={`/problem/${next.meta.id}`}>
                Next: {next.meta.title} <span aria-hidden="true">→</span>
              </Link>
            ) : (
              <Link className="text-link" to="/">
                Back to contents <span aria-hidden="true">→</span>
              </Link>
            )}
          </div>
        </div>

        <aside className="toc" aria-label="On this page">
          <p className="toc-label">On this page</p>
          {SECTIONS.map((section, index) => (
            <a
              key={section.id}
              href={`#${section.id}`}
              className={active === section.id ? 'is-active' : ''}
              aria-current={active === section.id ? 'location' : undefined}
              onClick={(event) => {
                event.preventDefault()
                const target = document.getElementById(section.id)
                if (target) target.scrollIntoView()
                const heading = document.getElementById(`${section.id}-title`)
                if (heading) {
                  heading.setAttribute('tabindex', '-1')
                  heading.focus({ preventScroll: true })
                }
                setActive(section.id)
              }}
            >
              <span className="toc-index">{String(index + 1).padStart(2, '0')}</span>
              {section.label}
            </a>
          ))}
        </aside>
      </div>
    </div>
  )
}

function SectionHead({ index, id, title }: { index: string; id: string; title: string }) {
  return (
    <div className="section-head">
      <span className="section-index" aria-hidden="true">
        {index}
      </span>
      <h2 id={id}>{title}</h2>
    </div>
  )
}
