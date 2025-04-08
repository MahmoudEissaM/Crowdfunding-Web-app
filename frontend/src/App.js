import React from 'react';
import Header from './components/header'; 
import Slider from './components/Slider';
import LatestProjects from './components/LatestProjects';
import FeaturedProjects from './components/FeaturedProjects';
import Categories from './components/Categories';
import SearchBar from './components/SearchBar';
import Footer from './components/footer';
const App = () => {
    return (
        <div className="homepage">
            <Header /> 
            <SearchBar />
            <Slider />
            <LatestProjects />
            <FeaturedProjects />
            <Categories />
            <Footer />
        </div>
    );
};

export default App;
