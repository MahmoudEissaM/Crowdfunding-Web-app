import React, { useState } from 'react';
import './css/searchBar.css';                      
const SearchBar = () => {
    const [query, setQuery] = useState('');

    const handleSearch = () => {
        window.location.href = `http://127.0.0.1:8000/search/?q=${query}`;
    };

    return (
        <div className="search-bar">
            <input
                type="text"
                className="search-input"
                placeholder="Search projects..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch} className="search-button">
                Search
            </button>
        </div>
    );
};

export default SearchBar;