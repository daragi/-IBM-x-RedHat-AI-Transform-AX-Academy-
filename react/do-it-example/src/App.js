import React from 'react'
import logo from './f.svg';
import './App.css';
import './App.js'


function getTitle(title) {
  return title;
}

const lists = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    phone: "1-770-736-8031 x56442",
    website: "hildegard.org",
    company: {
      name: "Romaguera-Crona",
      catchPhrase: "Multi-layered client-server neural-net",
      bs: "harness real-time e-markets"
    }
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    phone: "010-692-6593 x09125",
    website: "anastasia.net",
    company: {
      name: "Deckow-Crist",
      catchPhrase: "Proactive didactic contingency",
      bs: "synergize scalable supply-chains"
    }
  }
];

function List() {
  return (
    <div className="list-container">
      {lists.map(item => (
        <div key={item.id} className="list-card">
          <h3>{item.name} <small>({item.username})</small></h3>
          <p>📞 {item.phone}</p>
          <p>✉️ {item.email}</p>
          <p>🌐 <a href={`http://${item.website}`} target="_blank" rel="noreferrer">{item.website}</a></p>
          <p>🏢 {item.company.name}</p>
        </div>
      ))}
    </div>
  );
}
class Developer{
  constructor(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName;
  }
  getName() {
    let date = new Date().toLocaleTimeString()
    return this.firstName + ' ' + this.lastName + "("+ date + ")";
  }
}
const robin = new Developer("Robin", "Wieru")
console.log(robin.getName());
function App() {
  const storiese = [
    {
      title: "React",
      url: 'https://reatsjs.org',
      author: 'Jordan Walke',
      num_comments: 3,
      points: 4,
      objectID: 0,
    },
    {
      title: 'Redux',
      url: 'https://redux.js.org/',
      author: 'Dan Abramov, Andrew Clark',
      num_comments: 2,
      points: 5,
      objectID: 1,
    },
  ];
  let names = ["아 이 디", "비밀번호", "로그인", "다시입력"];
  const welcome = {
    greeting: 'Hey',
    title: 'React',
  };

  const numbers = [1, 4, 9, 16];
  const newNumbers = numbers.map(number => number * 2);
  console.log(newNumbers);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>별이 돌아가요</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          리 액 트 배 우 기
        </a>
      </header>
      <div className="content-container">
        <div className="login-box">
          <form action="home.html" className="login-form">
            <h2>로그인</h2>
            <div className="form-group">
              <label>{names[0]}</label>
              <input name="id" type="text" />
            </div>
            <div className="form-group">
              <label>{names[1]}</label>
              <input name="pwd" type="password" />
            </div>
            <div className="form-buttons">
              <input type="submit" value={names[2]} className="btn-submit" />
              <input type="reset" value={names[3]} className="btn-reset" />
            </div>
          </form>
        </div>

        <div className="list-section">
          <h2>회원 목록</h2>
          <List />
        </div>
      </div>
    </div>
  );
}

export default App;
