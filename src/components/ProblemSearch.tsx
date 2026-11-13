import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { problems } from '../lib/content'

export function ProblemSearch() {
  const [query, setQuery] = useState('')
  const [focused, setFocused] = useState(false)
  const navigate = useNavigate()
  const matches = query.trim()
    ? problems.filter((problem) => problem.meta.title.toLowerCase().includes(query.trim().toLowerCase())).slice(0, 8)
    : []
  const showResults = focused && query.trim().length > 0

  function openProblem(id: string) {
    setQuery('')
    setFocused(false)
    navigate(`/problem/${id}`)
  }

  return (
    <div
      className="problem-search"
      onBlur={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget)) setFocused(false)
      }}
    >
      <form
        role="search"
        onSubmit={(event) => {
          event.preventDefault()
          if (matches[0]) openProblem(matches[0].meta.id)
        }}
      >
        <label className="sr-only" htmlFor="problem-search-input">Search problems by name</label>
        <span className="search-icon" aria-hidden="true" />
        <input
          id="problem-search-input"
          type="search"
          autoComplete="off"
          placeholder="Search problems by name"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          onFocus={() => setFocused(true)}
          onKeyDown={(event) => {
            if (event.key === 'Escape') {
              setFocused(false)
              event.currentTarget.blur()
            }
          }}
          aria-controls="problem-search-results"
          aria-expanded={showResults}
        />
      </form>
      {showResults && (
        <div className="search-results" id="problem-search-results">
          {matches.length ? (
            <ul>
              {matches.map((problem) => (
                <li key={problem.meta.id}>
                  <Link to={`/problem/${problem.meta.id}`} onClick={() => { setQuery(''); setFocused(false) }}>
                    <span>{problem.meta.title}</span>
                    <span className="search-result-topic">{problem.topicName}</span>
                  </Link>
                </li>
              ))}
            </ul>
          ) : (
            <p>No problems found. Try another name.</p>
          )}
        </div>
      )}
    </div>
  )
}
