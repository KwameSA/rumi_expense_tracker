# Rumi Expense and Book Tracker

A Django web application for managing personal finances and book inventory. Users can record, edit, and delete expenses, as well as add, edit, and remove books. The app is containerized with Docker and designed for scalable deployment.

---

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Technologies Used](#technologies-used)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)   
- [License](#license)  
- [Links](#links)  

---

## Features(#features)

- Track expenses: create, update, and delete transactions  
- Manage books: full CRUD for book inventory  
- Containerized deployment using Docker  
- PostgreSQL database backend for reliable data storage  
- Scalable structure ready for future analytics dashboards  
- Optional: Multi-user support for shared access  

---

## Project Structure
```
rumi_expense_tracker/
├── books/ # Django app for books management
├── expenses/ # Django app for expense tracking
├── rumipress/ # Project settings and WSGI configuration
├── static/ # Frontend static files
├── templates/ # HTML templates
├── Dockerfile # Docker container configuration
├── docker-compose.yml # Docker Compose services
├── requirements.txt # Python dependencies
└── manage.py # Django management script
```

---

## Technologies Used

- **Backend:** Python, Django, PostgreSQL  
- **Frontend:** HTML, CSS, Django Templates  
- **Deployment:** Docker, Docker Compose, Gunicorn  
- **Tools:** Git, GitHub, Railway (for hosting)  

---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/KwameSA/rumi_expense_tracker.git
cd rumi_expense_tracker
```

2. Create a .env file with your environment variables
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://username:password@localhost:5432/dbname
```
3. Build and run the Docker containers
```
docker-compose up --build
```
4. Apply migrations
```
docker-compose run web python manage.py migrate
```
5. Collect static files
```
docker-compose run web python
manage.py collectstatic
```
6. Access the app
```
Open http://localhost:8000 in your browser.
```
---
Usage
- Navigate to /books/ to manage book inventory

- Navigate to /reports/ to gain insights on what

- Use CRUD operations to add, edit, or delete entries
---
Screenshots
- [Visit Portfolio](https://kwamesa.github.io/portfolio/index.html)
---
Links
- Live App: [Rumi Expense Tracker](https://rumiexpensetracker-production.up.railway.app/books/)

