# Crowdfunding Web App

A full-stack crowdfunding platform built using **Django**. Users can create and support projects, manage their profiles, and explore campaigns created by others — all through a clean and responsive interface.

---
## 🚀 Features

- User authentication and authorization
- Create, list, and view project details
- View and manage your profile (edit info, see your donations/projects, delete account)
- Responsive homepage

## 👥 Team Members

- **Mahmoud & Mohamed** – Authentication (backend & frontend)
- **Sara** – Homepage design and implementation
- **Reham & Nadia** – Projects: create, list, and detail views

## 🛠️ Tech Stack
### 🎨 Frontend

- **Django Templates**  
  Built-in Django templating engine used to render dynamic HTML pages directly from the backend.

- **HTML5 & CSS3**  
  Structure and style for the user interface, following modern web standards.

- **Bootstrap**  
  Frontend framework for responsive design and pre-built UI components (buttons, navbars, grids, etc.).

- **JavaScript (vanilla)**  
  Used for basic client-side interactivity where needed (e.g., form validation, toggling content).

### 🔙 Backend

- **Django 3.2**  
  Web framework for building backend APIs with features like ORM, routing, admin interface, and authentication.

- **WhiteNoise**  
  Helps serve static files (CSS, JS, images) directly from Django, simplifying deployment.

- **Python Decouple**  
  Manages environment variables and keeps sensitive info like `SECRET_KEY` outside the source code.

- **dj-database-url**  
  Parses database URLs into Django-compatible database configurations. Useful for deployment setups.

---

### 🧰 Dev Tools & Formatting

- **Unipath**  
  Simplifies and cleans up file path handling in Python projects.

- **sqlparse**  
  A SQL formatting library used internally by Django for parsing and pretty-printing SQL statements.

- **Pillow**  
  Image processing support used for handling uploads like profile pictures or project thumbnails.


## 📦 Installation & Setup

> Clone the repo and set up the project locally

---

### 1. Clone the Repository

```bash
git clone https://github.com/MahmoudEissaM/Crowdfunding-Web-app
cd Crowdfunding-Web-app
```
### 2. Backend Setup (Django)

```bash
python -m venv env
source env/bin/activate 
pip install -r requirements.txt
```
### 3. Apply Migrations & Run the Development Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver #Check port's availability
