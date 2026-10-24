import { HashRouter, Route, Routes } from 'react-router-dom'
import { Layout } from '../components/Layout'
import { Home } from '../pages/Home'
import { NotFound } from '../pages/NotFound'
import { Problem } from '../pages/Problem'
import { Topic } from '../pages/Topic'

export function App() {
  return (
    <HashRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="topic/:topicId" element={<Topic />} />
          <Route path="problem/:problemId" element={<Problem />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </HashRouter>
  )
}
