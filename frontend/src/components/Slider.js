import React, { useEffect, useState } from 'react';
import './css/Slider.css';

const Slider = () => {
    const [projects, setProjects] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/top-rated-projects/')
            .then((response) => response.json())
            .then((data) => {
                // Filter and sort to get the top 5 highest-rated running projects
                const topProjects = data
                    .filter((project) => project.is_running) // Only running projects
                    .sort((a, b) => b.rating - a.rating) // Sort by rating (highest first)
                    .slice(0, 5); // Take the top 5
                setProjects(topProjects);
            });
    }, []);

    const handleNext = () => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % projects.length);
    };

    const handlePrevious = () => {
        setCurrentIndex((prevIndex) => (prevIndex - 1 + projects.length) % projects.length);
    };

    return (
        <div className="slider">
            {projects.length > 0 && (
                <div className="slide">
                    <img
                        src={`http://127.0.0.1:8000/media/${projects[currentIndex].image_url}`} // Prepend media URL
                        alt={projects[currentIndex].title}
                        className="slide-image"
                    />
                    <h3>{projects[currentIndex].title}</h3>
                    <p>{projects[currentIndex].description}</p>
                    <p>Rating: {projects[currentIndex].rating}</p>
                </div>
            )}
            <div className="slider-controls">
                <button onClick={handlePrevious} className="slider-button">
                    Previous
                </button>
                <button onClick={handleNext} className="slider-button">
                    Next
                </button>
            </div>
        </div>
    );
};

export default Slider;