import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';

const welcome = {
  greeting: 'Hey',
  title: 'React',
};
function getTitle(title){
  return title;
};
const list = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net"
  },
];
function List(){
  return list.map(function(item){
    return (
          <div key={item.id}>
              <span>name1 : {item.name}</span>
              <span>name2 : {item.username}</span>
              <span>phone : {item.phone}</span>
              <span>website : 
                <a href='http://{item.website}'>
                      {item.website}</a></span>
              <span>email : {item.email}</span>          
          </div>
    );
  });
}
class Developer extends React.Component {
  constructor(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName;
  } 
  getName(){
    let date = new Date().toLocaleTimeString()
    return this.firstName 
    + " " + this.lastName
    + " (" + date + ")";
  }
}
<></>
const robin = new Developer("Robin", "Wieruch");
console.log(robin.getName());
function App() {
  let names = ["아 이 디", "비밀번호", "로그인", "다시입력"];
  const tableStyle = {
    backgroundColor:'yellow',
    fontSize: '20px',
  };

  const numbers = [1,4,9,16];
  const newNumbers = numbers.map(function(numbers){
    return numbers * 2;
  });
  console.log(newNumbers);
  return (
<div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          리액트 배우기2 
        </a>
      </header>
      <div>
        <h1>{welcome.greeting}
            {getTitle('리액트')}
        </h1>
        <hr />
        <span>이름</span><span>전화번호</span><span>홈페이지</span><span>email</span>
        <List />
        <form action="home.html" >
              <table border="1" style={tableStyle}>
                  <tr>
                      <td className="App-id">{names[0]}</td><td><input name="id"></input></td>
                  </tr>
                  <tr>
                      <td className="App-pwd">{names[1]}</td><td><input name="pwd"></input></td>
                  </tr>
                  <tr>
                      <td colspan="2">
                          <input type="submit" value={names[2]} >
                          </input>
                          <input type="reset" value={names[3]}></input>
                      </td>
                  </tr>
              </table>
          </form>
      </div>
    </div>
  );
  // const a = 0;
  // console.log1(a);


}
// 이름없는 함수
count => {
  return count + 1;
}
// in-line 함수
count => count + 1;

export default App_1;
