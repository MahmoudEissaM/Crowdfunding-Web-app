import React, { useEffect, useState } from 'react';
import './css/Categories.css'; // Import the CSS file for styling

const Categories = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/categories/') // Replace this endpoint
            .then((response) => response.json())
            .then((data) => setCategories(data));
    }, []);

    return (
        <div className="categories">
            <h2 className="categories-title">Categories</h2>
            <ul className="categories-list">
                {categories.map((category) => (
                    <li key={category.id} className="categories-item">
                        <a href={`/category/${category.id}/`} className="categories-link">
                            {category.name}
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Categories;