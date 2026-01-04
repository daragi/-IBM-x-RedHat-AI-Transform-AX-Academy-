import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';
const App = () => {
  const stories = [
    {
      title: 'React',
      url: 'https://reactjs.org/',
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
  const [searchTerm, setSearchTerm] = React.useState(''); 
  const handleSearch = event => {
    setSearchTerm(event.target.value);
  };
  const searchStories = stories.filter(function(story){
    return story.title.toLowerCase()
    .includes(searchTerm.toLowerCase());
  });
  return (
    <div>
      <h1>My Hacker Stories</h1>
      <Search onSearch={handleSearch}/>

      <hr />

      <List list={searchStories} />
    </div>
  );
};

const Search = (props) => (
  <div>
       <label htmlFor="search">Search: </label>
       <input id="search" type="text" onChange={props.onSearch} />
  </div>
);

// const Search = (props) => {
//   //객체 데이터에 대한 getter/setter를 만든다.
//   const [searchTerm, setSearchTerm] = React.useState(''); 
//   //이벤트기반의 생명주기를 가지도록 만든다.
//   const handleChange = (event) => {
//     // setSearchTerm(event.target.value);
//     props.onSearch(event)
//   };
//   return(
//     <div>
//       <label htmlFor="search">Search: </label>
//       <input id="search" type="text" onChange={props.onSearch} />

//       <p>
//         Searching for <strong>{searchTerm}</strong>.
//       </p>
//     </div>
//   );
// };
const List = (props) => (
  <ul>
    {props.list.map((item) => (
      <li key={item.objectID}>
        <span>
          <a href={item.url}>{item.title}</a>
        </span>
        <span>{item.author}</span>
        <span>{item.num_comments}</span>
        <span>{item.points}</span>
      </li>
    ))}
  </ul>
);

export default App;