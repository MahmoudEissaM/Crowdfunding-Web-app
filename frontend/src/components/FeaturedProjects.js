import React, { useEffect, useState } from 'react';
import './css/FeaturedProjects.css'; // Import the CSS file for styling

const FeaturedProjects = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/featured-projects/') // Replace this endpoint
            .then((response) => response.json())
            .then((data) => setProjects(data));
    }, []);

    return (
        <div className="featured-projects">
            <h2 className="featured-projects-title">Featured Projects</h2>
            <ul className="featured-projects-list">
                {projects.map((project) => (
                    <li key={project.id} className="featured-project-item">
                        <h3 className="project-title">{project.title}</h3>
                        <p className="project-description">{project.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FeaturedProjects;