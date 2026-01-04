import "./App.css";
import React from "react";
import { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import logo from "./f.svg"

function Login() {
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async () => {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `loginId=${encodeURIComponent(id)}&pwd=${encodeURIComponent(password)}`
    });

    if (response.ok) {
      const data = await response.json();
      setMessage(`환영합니다, ${data.userName}님!`);
    } else {
      const error = await response.json();
      setMessage("X" + error.detail);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>로그인</h2>
      <input
        type="text"
        placeholder="아이디"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="비밀번호"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br />
      <button onClick={handleLogin}>로그인</button>
      <h4>{message}</h4>
    </div>
  );
}

function App() {
  const [message, setMessage] = useState("");
  const [ending, setEnding] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/hello")
      .then((response) => response.json())
      .then((json) => {
        setMessage(json.message);
        setEnding("OK");
      })
      .catch((error) => {
        console.error("Error:", error);
        setEnding("Error");
      });
  }, []);
  return (
    <div>
      <div>
        <span>Hello Server</span>
        <h1>{message}</h1>
        <p>{ending}</p>
      </div>
      <Login />
    </div>
  );
}

export default App;
