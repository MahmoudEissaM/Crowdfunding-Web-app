# Crowdfunding Web App

A full-stack crowdfunding platform built with **Django** and **React**. Users can create and support crowdfunding projects, manage their profiles, and explore and donate to campaigns created by others.

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

- **Frontend**: React,
- **Backend**: Django, Django REST Framework
- **Database**: SQLite

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
