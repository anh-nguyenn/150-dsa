import { useEffect } from 'react'
import { Link, Outlet, useLocation } from 'react-router-dom'
import { problems } from '../lib/content'
import { isStorageAvailable, solvedCount, useProgress } from '../lib/progress'

function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'auto' })
  }, [pathname])
  return null
}

export function Layout() {
  const progress = useProgress()
  const solved = solvedCount(progress)
  const total = problems.length

  return (
    <div className="site">
      <a
        className="skip-link"
        href="#main"
        onClick={(event) => {
          event.preventDefault()
          const main = document.getElementById('main')
          if (main) {
            main.focus()
            main.scrollIntoView()
          }
        }}
      >
        Skip to content
      </a>
      <ScrollToTop />
      <header className="site-header">
        <div className="header-inner">
          <Link to="/" className="wordmark" aria-label="150, home">
            <span className="wordmark-number">150</span>
            <span className="wordmark-rule" aria-hidden="true" />
            <span className="wordmark-label">algorithm study</span>
          </Link>
          <div className="header-meta">
            <span className="header-count">
              <span className="header-count-value">{solved}</span>
              <span className="header-count-sep">/</span>
              <span>{total}</span>
            </span>
            <span className="header-count-label">solved</span>
          </div>
        </div>
      </header>

      {!isStorageAvailable() && (
        <div className="storage-banner" role="status">
          Storage is blocked in this browser. Progress will last for this tab only.
        </div>
      )}

      <main id="main" tabIndex={-1}>
        <Outlet />
      </main>

      <footer className="site-footer">
        <div className="footer-inner">
          <p>Unaffiliated study project. Problems belong to LeetCode.</p>
          <p className="footer-note">Built for one learner. Local-first, no account.</p>
        </div>
      </footer>
    </div>
  )
}
