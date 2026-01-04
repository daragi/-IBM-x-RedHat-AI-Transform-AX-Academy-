import 'bootstarp/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";
import React from 'react';
import {Link} from 'react-router-dom';
function Header(props) {
    return (
        <div> 
            <main>
            <Link to="/"> <h1>홈으로</h1> </Link>
            <Link to="/login.html"> <h4>logIn</h4></Link>
            </main>
        </div>
    );
}
export default Header;