import React, { useEffect, useState } from 'react';
import './css/LatestProjects.css'; // Import the CSS file for styling

const LatestProjects = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        // Replace API call with fake data for testing
        const fakeData = [
            { id: 1, title: 'Project Alpha', description: 'Description of Project Alpha' },
            { id: 2, title: 'Project Beta', description: 'Description of Project Beta' },
            { id: 3, title: 'Project Gamma', description: 'Description of Project Gamma' },
            { id: 4, title: 'Project Delta', description: 'Description of Project Delta' },
        ];
        setProjects(fakeData);
    }, []);

    return (
        <div className="latest-projects">
            <h2 className="latest-projects-title">Latest Projects</h2>
            <ul className="latest-projects-list">
                {projects.map((project) => (
                    <li key={project.id} className="latest-project-item">
                        <h3>{project.title}</h3>
                        <p>{project.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default LatestProjects;