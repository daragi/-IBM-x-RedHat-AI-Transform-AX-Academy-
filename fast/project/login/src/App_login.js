import React from 'react';
import ReactDOM from 'react';
import logo from './f.svg';
import './App.css';

const App = () => {
  const users = [
    {
      "id": 1,
      "name": "Leanne Graham",
      "password": "1234",
      "email": "Sincere@april.biz",
      "phone": "1-770-736-8031 x56442",
      "website": "hildegard.org"
    },
    {
      "id": 2,
      "name": "Ervin Howell",
      "password": "0000",
      "email": "Shanna@melissa.tv",
      "phone": "010-692-6593 x09125",
      "website": "anastasia.net"
    },
  ];
 
  const [loginTerm, setLoginTerm] = React.useState(''); 
  const [loginPass, setLoginPass] = React.useState('id first'); 
  const handlelogin = event => {
    // event.target == id ->setLoginTerm(), pwd -> setLoginPass()
    (event.target == document.getElementById("id"))?
          loginUserId(event.target.value):
          setLoginPass(event.target.value);
  };
  const loginUserId = users.filter(function(user){
    return (user.email.toLowerCase().includes(loginTerm.toLocaleLowerCase()))? user.email : "";

  });
  const loginUserPassword = users.filter(function(user){
    return (loginUserId != "")?user.password.includes(loginTerm):"";
  });
  return (
    <div>
      <h1>My Login Page</h1>
      <Login onLogin={handleLogin}/>

      <hr />

      <List list={loginUserPassword} />
    </div>
  );
};

const Login = (props) => (
  <div>
    <label htmlFor="login">Login</label><br/>
    [ID] <input id="email" type="text" onChange={props.onLogin} />&nbsp;&nbsp;
    [PASSWORD] <input id="password" type="text" onChange={props.onLogin}/>
  </div>
);
//  로그인 처리시 사용자 정보 출력력
const List = (props) => (
  <ul>
    {props.list.map((item) => (
      <li key={item.id}>
        <span>{item.email}</span>&nbsp;&nbsp;&nbsp;
        <span>{item.name}</span>&nbsp;&nbsp;&nbsp;
        <span>{item.phone}</span>&nbsp;&nbsp;&nbsp;
        <span>{item.website}</span>
      </li>
    ))}
  </ul>
);

export default App;