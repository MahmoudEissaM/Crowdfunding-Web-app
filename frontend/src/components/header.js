import React from 'react';
import './css/header.css'; 

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <a href="/">Crowdfunding</a>
            </div>
            <nav className="nav">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/projects">Projects</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
            <div className="auth">
                <a href="/login" className="login">Login</a>
                <a href="/signup" className="signup">Sign Up</a>
            </div>
        </header>
    );
};

export default Header;