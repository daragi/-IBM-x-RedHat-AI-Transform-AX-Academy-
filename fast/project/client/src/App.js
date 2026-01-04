import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';
const App = () => {
  return (
    <div>
      <h1>My Hacker Stories</h1>
      <a href='http://localhost:8000'>hello</a>

      <form method='put' action='http://localhost:8000/items/2'>
        이름 : <input name="q"></input><br></br>
        가격 : <input name="price"></input><br></br>        
        주문 : <input name="is_offer"></input><br></br>
        <hr/>
        <input type="submit" value={'Update'}></input>
      </form>
    </div>
  );
};

export default App;