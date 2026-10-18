# fullstack_developer_capstone

Repository: **xrwvm-fullstack_developer_capstone**

Welcome to the **Dealerships Application**, a full-stack web application developed as part of the IBM Full Stack Cloud Developer Capstone Project.

## Project Overview

The Dealerships Application allows users to browse a national directory of car dealerships, view dealership information and reviews, and submit reviews with sentiment analysis. The system is designed with a modern microservices architecture that combines Django for user management and backend routing, Node.js/Express for dealership and review data services, and React for a dynamic, responsive user interface.

## Key Features

- **Dealership Directory**: Browse dealerships across all US states or filter by specific states (e.g., Kansas, Texas, California).
- **Dealer Details & Customer Reviews**: View comprehensive dealership information alongside real customer reviews.
- **Sentiment Analysis**: Automated sentiment classification (positive, neutral, negative) for customer reviews.
- **Review Submission**: Authenticated users can submit reviews for cars purchased, specifying make, model, year, and purchase date.
- **Authentication System**: User registration, login, and session persistence backed by Django authentication.
- **Static Information Pages**: Professional 'About Us' and 'Contact Us' pages showcasing company background and support channels.

## Architecture & Technology Stack

- **Backend Web Framework**: Python Django 6.1.1
- **Database & Microservices**: Node.js & Express.js microservices serving dealership and review data (JSON).
- **Frontend**: React.js SPA with Bootstrap 5 and custom CSS styling.
- **Database**: SQLite3 for user authentication; JSON document store for dealerships and reviews.
- **CI/CD Workflow**: GitHub Actions with multi-job workflows for Python (flake8) and JavaScript (ESLint) linting.
- **Deployment**: IBM Cloud Code Engine / Skills Network Cloud IDE HTTPS proxy.

## Project Structure

```
xrwvm-fullstack_developer_capstone/
├── server/
│   ├── database/          # Node.js Express dealership & review microservices
│   ├── djangoapp/         # Django application (views, models, routes)
│   ├── djangoproj/        # Django project settings and root URLs
│   └── frontend/          # React frontend application & static assets
├── CICD                   # CI/CD workflow logs
├── deploymentURL          # Active deployment URL
└── README.md              # Project documentation
```

## Running the Application

1. **Start the Express Microservice**:
   ```bash
   cd server/database
   node app.js
   ```

2. **Start the Django Development Server**:
   ```bash
   cd server
   python manage.py runserver 8000
   ```

3. **Access the Application**:
   Navigate to `http://localhost:8000/` or your assigned cloud deployment URL.