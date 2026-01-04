import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';


  
const AppPs = () => {
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
      const initialStories = [
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
const getAsyncStories = () =>
    new Promise(resolve=>
        setTimeout(() => resolve({data : {stories: initialStories}}),
        2000));
// promise = 상황에 따라 동작할 거야, 비동기 처리에 활용되는 객체
// 비동기 로직을 마치 동기로직처럼 사용할 수 있는 기능
// sync vs. async : data broken => set, add, update, delete vs. get은 data변형과 상관없음
const [stories, setStories] = React.useState(initialStories);
const [isLoading, setIsLoading] = React.useState(false);

React.useEffect(()=> {
    setIsLoading(true);
    getAsyncStories().then(result => {
        setStories(result.data.stories);
        setIsLoading(false);
    });
},[]);
const handleRemoveStory = item => {
    const newStories = stories.filter(
        story => item.objectID != story.objectID
    );
    setStories(newStories);
};

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

const List = ({list, onRemoveItem}) => 
list.map(item => 
<Item 
 key={item.objectID} 
 item={item}
 onRemoveItem={onRemoveItem} />);

const Item = ({item, onRemoveItem}) => {
    const handleRemoveItem = () => {
        onRemoveItem(item);
    };
    return(
        <div>
        <span>
          <a href={item.url}>{item.title}</a>
        </span>
        <span>{item.author}</span>
        <span>{item.num_comments}</span>
        <span>{item.points}</span>
        <span>
            <button type="button" onClick={handleRemoveItem}>
                Dismiss
            </button>
        </span>
      </div>
    )

};
 

  const useSemiPersistentState = (key, initializeState) => {
    const [value, setValue] = React.useState(
      localStorage.getItem(key)||initializeState);
    React.useEffect(() => {
      localStorage.setItem(key, value);
      console.log(key);
      console.log(value);
    }, [value, key]);
    
  return [value, setValue] ;
  };

  const [searchTerm, setSearchTerm]
       = useSemiPersistentState("search", "React");

  const handleSearch = event => {
    setSearchTerm(event.target.value);
  };

const InputWithLabel = ({
    id, 
    children, 
    value, 
    type='text', 
    isFocused, // isfocused="true" -> getter, autoFocus -> setter
    onInputChange}) => {
      const inputRef = React.useRef();
      React.useEffect(()=>{
        if(isFocused && inputRef.current){
          inputRef.current.focus();
        };
      }, [isFocused]);
      return (
        <>
          <label htmlFor={id}>{children}</label>
          &nbsp;
          <input
              ref={inputRef} 
              id={id} 
              type={type} 
              value={value} 
              autoFocus = {isFocused} //-> getter, autoFocus -> setter
              onChange={onInputChange} />
        </>
      );
};
  const searchStories = initialStories.filter(function(story){
    console.log('searchStories', initialStories);
    console.log('initialStories', initialStories);
    return story.title.toLowerCase()
    .includes(searchTerm.toLowerCase());
  });
  return (
    <div>
      <h1>My Hacker Stories</h1>
      <Search search={searchTerm} onSearch={handleSearch}/> 
          {/* 를 살리고 Search 컴포넌트 안에서 InputWithLabel를 사용토록 수정해볼 것! */}
      {/* <InputWithLabel id="search" label="Search" value={searchTerm} onInputChange={handleSearch}>
        <strong>검색 : </strong>
      </InputWithLabel> */}
      <hr />

      <List list={searchStories} onRemoveItem={handleRemoveStory} />
    </div>
  );
};

export default AppPs;