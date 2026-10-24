# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

React + Vite + TypeScript, static build. Pyodide runs in a Web Worker. Content is Markdown, JSON, and Python compiled at build time. Hosted on GitHub Pages; local development is the primary environment.

## Users

One solo developer-learner working through NeetCode 150 at a desk in focused sessions, often after a failed attempt or before an interview. The job is to understand the pattern well enough to reproduce the optimal solution from scratch, not to collect accepted answers.

## Product Purpose

Turn each NeetCode 150 problem into a complete lesson: an own-words summary, plain-language background, progressive hints, brute-force-to-optimal solutions with complexity, a runnable Python editor, and a hand-authored execution visualization. Success is being able to explain and re-implement the optimal approach without looking.

## Positioning

The step-through visualization is the teaching mechanism, not an add-on. Each trace is generated from the reference solution itself, so what the learner watches is the algorithm they are reading, checked against the same tests. Hand-authored captions are the next refinement.

## Operating Context

Long desktop study sessions, with occasional phone-width review. Authoring happens in the repository with local scripts. No login, no backend, no server state. Progress and code live in the browser.

## Capabilities and Constraints

- 150 problems in 18 topics, in NeetCode order.
- All 150 lessons exist at the minimum viable tier: description with structured examples and constraints, background, three hints, one optimal solution, starter code, and authored tests.
- The problem page is a practice-first split: description left, editor and authored testcase runner right, Learn material below.
- One optimal approach per problem at the minimum tier, with time and space. Brute-force contrasts are later upgrades.
- Python execution in the browser through Pyodide, loaded lazily.
- A test runner with per-problem comparison modes and adapters for linked lists, trees, and graphs.
- Visualizations are precomputed execution traces generated from each reference solution and played in a shared step-through player. They do not visualize custom inputs or the learner's own code; hand-authored captions are a later upgrade.
- Testcases are authored and read-only; Run uses one selected case, Submit uses all cases.
- Progress is stored locally; the site must work when storage is unavailable.
- Problem text is written in original words; LeetCode is linked, never copied.
- Static hosting only.

## Brand Commitments

Unaffiliated study project. No LeetCode or NeetCode branding, logos, or copied content.

## Evidence on Hand

PLAN.md and this product brief. The repository contains 150 written and verified lessons, the React application, local progress storage, a working Pyodide test runner, and generated execution traces with a shared visualizer. It does not contain user data, testimonials, or usage claims.

## Product Principles

- Understanding over completion. A solved checkmark is not the goal; recall is.
- Authoring throughput is a first-class constraint. Every system decision must reduce the cost of the next problem.
- Verify, do not trust. Every solution and every visual is executed and compared against the same tests.
- The interface disappears behind the problem. Chrome, motion, and color earn their place by helping the learner read the algorithm.
- Local-first and zero-account. The site works without a backend and degrades cleanly without storage.

## Accessibility & Inclusion

The editor, player, and navigation are keyboard-operable. Visualizations respect prefers-reduced-motion and expose the current frame as text. Content is readable at 390px and at desktop widths.
