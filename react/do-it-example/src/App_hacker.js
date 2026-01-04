import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';

const InputWithLabel = 
({id,
  label, 
  value, 
  type="text", //hard coding, immutable
  isFocused, // isfocused="true"  -> getter, autoFocus -> setter
  onInputChange}) => (
  <>
    <label htmlFor={id}>{label}</label>
    &nbsp;
    <input id={id} type={type} value={value} onChange={onInputChange}></input>
  </>
);

const AppHacker = () => {
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
  // const [searchTerm, setSearchTerm] = 
  // React.useState(localStorage.getItem('search') || 'React');

  // React.useEffect(() => {
  //   localStorage.setItem('search', searchTerm);
  // });
  const handleSearch = event => {
    setSearchTerm(event.target.value);
  };
  
  const [searchTerm, setSearchTerm] = useSemiPesrsistentState('search', 'React');
  const searchStories = stories.filter(function(story){
    return story.title.toLowerCase()
    .includes(searchTerm.toLowerCase());
  });

  return (
    <div>
      <h1>My Hacker Stories</h1>
      {/* <Search search={searchTerm} onSearch={handleSearch}/> */}
      <InputWithLabel id="search" label ="Search" value={searchTerm}
      isFocused
      onInputChange={handleSearch}>
      </InputWithLabel>
      <hr />

      <List list={searchStories} />
    </div>
  );
};
// AppHacker {} 안에 들어 있는 컴포넌트 들은 App과에 부모자식 관계를가짐 => 상속
// App has a handleSearch 같은 표현이 가능

const Search = (props) => {
  //객체 데이터에 대한 getter/setter를 만든다.
  const [searchTerm, setSearchTerm] = React.useState(''); 
  //이벤트기반의 생명주기를 가지도록 만든다.
  const handleChange = (event) => {
    // setSearchTerm(event.target.value);
    props.onSearch(event)
  };
  return(
    <div>
      <label htmlFor="search">Search: </label>
      <input id="search" type="text" onChange={props.onSearch} />

      <p>
        Searching for <strong>{searchTerm}</strong>.
      </p>
    </div>
  );
};

const useSemiPesrsistentState = (key, initalizeState) => {
  const [value, setValue] = React.useState(
    localStorage.getItem(key) || initalizeState);
  React.useEffect(() => {
    localStorage.setItem(key, value);
    console.log(key); 
    console.log(value); 
    // 'search'를 searchTerm에 저장
    // set 을 불러오기 위해서 set의 key값 필요(중복제거 외에? 하는게 없음)
    // 리스트의 값을 찾기 위해 사용하는 index와 비슷함
    // 그렇기에 map을 활용하여 키 값을 찾음 setItem('search',searchTerm) 이 구조는 맵구조와 같음
  }, [value, key]); // searchTerm 값을 통해 state or effect에 접근이 가능
  return [value, setValue]; // hook function, useState, useEffect이벤트와 연결
};

const List = ({list}) => // static library = 정적 라이브러리
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

export default AppHacker;

