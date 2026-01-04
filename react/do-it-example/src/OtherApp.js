import logo from './f.svg';
import './App.css';
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'
import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';
import Products from './components/Products';
import NotFound from './components/NotFound';

function OtherApp() {
    return(
        <div>
            <BrowserRouter>
                <Header/>
                <Routes>
                    <Route path='/' element={<Main/>}></Route>
                    <Route path="/products/:productId" element={<Products/>}></Route>
                    <Route path='*' element={<NotFound/>}></Route>
                </Routes>
                <Footer/>
            </BrowserRouter>
        </div>
    )
}

export default OtherApp;