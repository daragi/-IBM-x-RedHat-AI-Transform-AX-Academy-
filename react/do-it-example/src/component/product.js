import React from 'react';
import {useParams} from 'react-router-dom';
import {useLocation} from 'react-router-dom';

const Product = (props) => {
    const productId = useParams().productId;
    const location = useLocation();
    return (
        <div>
            <h3>{productId}진열 상품</h3>
            <ul>
                <li> 제품 : {location.hash}</li>
                <li> 위치 : {location.pathname}</li>
                <li> 검색 : {location.search}</li>
                <li> 상태 : {location.state}</li>
            </ul>
        </div>
    )
}

export default Product;