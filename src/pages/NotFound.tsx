import { Link } from 'react-router-dom'
import { useDocumentTitle } from '../lib/useDocumentTitle'

export function NotFound() {
  useDocumentTitle('Not found · 150')
  return (
    <div className="page not-found">
      <p className="kicker">404</p>
      <h1>This page is not in the catalog.</h1>
      <p className="not-found-copy">
        The link may be old, or the problem may live under a different topic. The contents page is the shortest way
        back.
      </p>
      <Link className="btn btn-primary" to="/">
        Back to contents <span aria-hidden="true">→</span>
      </Link>
    </div>
  )
}
