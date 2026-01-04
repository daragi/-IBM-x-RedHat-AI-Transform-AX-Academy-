import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';
const App = () => {
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
  const [searchTerm, setSearchTerm] = React.useState('react'); 
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
      <Search search={searchTerm} onSearch={handleSearch}/>

      <hr />

      <List list={searchStories} />
    </div>
  );
};

const Search = ({search, onSearch}) => {
  <div>
       <label htmlFor="search">Search: </label>
       <input id="search" 
        type="text" 
        value = {search}
        onChange={onSearch} />
  </div>
};

const List = ({list}) => 
  list.map(item => <Item key={item.objectID} item={item} />);

  const Item = ({item}) => (
    <div>
      <span>
        <a href={item.url}>{item.title}</a>
      </span>
      <span>{item.author}</span>
      <span>{item.num_comments}</span>
      <span>{item.points}</span>
    </div>
  );

export default App;