# Django API Project

This project is a Django-based API designed to manage spiritual events and places. It allows users to add, search, and filter events and places by faith, location, and radius.

## Table of Contents

1. [Project Setup](#project-setup)
2. [API Endpoints](#api-endpoints)
3. [How to Run the Project](#how-to-run-the-project)

## Project Setup

To set up the project locally, follow these steps:

### 1. Clone the Project

If the project is hosted on a Git repository, clone it using the following command:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Run migrations to apply the database schema:

```bash
python manage.py migrate
```

### 5. Collect Static Files

Collect static files (CSS, JavaScript, images) needed for the frontend:

```bash
python manage.py collectstatic --noinput
```

## API Endpoints

### 1. / (Home Route)

Base URL: https://masterverses-production.up.railway.app

- **View**: `api_home`
- **Name**: `api-home`
- **Description**: The home route for the API. It allows users to:
  - Search for spiritual events and places
  - Filter results by faith/religion
  - Filter places by radius
  - Automatically detect the user's location or let them input it manually

### 2. /add-event

- **View**: `add_event`
- **Name**: `add-event`
- **Description**: Adds a new spiritual event. This endpoint accepts POST requests to create a new event in the database.

### 3. /api/events/

- **View**: `SpiritualEventsView` (Class-based view)
- **Name**: `spiritual-events`
- **Description**: Fetches all spiritual events in the database. You can use filters for faith, radius, and other attributes if needed.

### 4. /api/spiritual-places/

- **View**: `NearbySpiritualPlacesView` (Class-based view)
- **Name**: `spiritual-places`
- **Description**: Retrieves a list of nearby spiritual places based on geolocation. Filters for faith and radius are supported.

## How to Run the Project

### Run the Development Server

1. **Start Django Development Server**: Run the following command to start the development server:

   ```bash
   python manage.py runserver
   ```

2. **Access the API**: The API will be available on http://127.0.0.1:8000/ (or another configured host).

3. **Interact with the API**:
   - `GET /api/events/`: Fetch all events
   - `GET /api/spiritual-places/`: Fetch spiritual places (can provide location data)
   - `POST /add-event`: Create a new event by sending data in the request body

## Deployment Instructions

### Prepare for Deployment

1. **Set Environment Variables**: Make sure to set any necessary environment variables, like `DJANGO_SECRET_KEY`, `DATABASE_URL`, etc., either locally or through your hosting platform's dashboard.

2. **Prepare for Deployment on Railway/Heroku**:

   For a smooth deployment on platforms like Railway or Heroku, the following steps will be necessary.

### Deployment Script

The following deployment command installs dependencies, applies migrations, collects static files, and starts the application using Gunicorn.

```json
{
  "deploy": {
    "startCommand": "pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn masterverses.wsgi --bind 0.0.0.0:$PORT"
  }
}
```

### Steps to Deploy:

1. **Install Dependencies**: Ensure that all required Python dependencies are installed:

   ```bash
   pip install -r requirements.txt
   ```

2. **Apply Migrations**: Apply any database migrations that are required for your models:

   ```bash
   python manage.py migrate
   ```

3. **Collect Static Files**: Collect static files needed for frontend:

   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Start the Application**: Start the application with Gunicorn, which will bind the application to the provided port:

   ````bash
   python manage.py runserver   ```
   ````
