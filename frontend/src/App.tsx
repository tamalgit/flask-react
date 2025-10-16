import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [hello, setHello] = useState<string>('')
  const [echoResponse, setEchoResponse] = useState<string>('')

  async function callHello() {
    try {
      const res = await fetch('/api/hello')
      const json = await res.json()
      setHello(JSON.stringify(json))
    } catch (e) {
      setHello('error')
    }
  }

  async function callEcho() {
    try {
      const res = await fetch('/api/echo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ from: 'frontend', at: new Date().toISOString() })
      })
      const json = await res.json()
      setEchoResponse(JSON.stringify(json))
    } catch (e) {
      setEchoResponse('error')
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
        <div style={{ display: 'flex', gap: 12, marginTop: 12 }}>
          <button onClick={callHello}>Call /api/hello</button>
          <button onClick={callEcho}>Call /api/echo</button>
        </div>
        <pre style={{ textAlign: 'left', background: '#222', color: '#0f0', padding: 8, borderRadius: 4, marginTop: 12 }}>
{hello || 'hello: (no data)'}
        </pre>
        <pre style={{ textAlign: 'left', background: '#222', color: '#0f0', padding: 8, borderRadius: 4, marginTop: 12 }}>
{echoResponse || 'echo: (no data)'}
        </pre>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
