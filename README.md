# API Gateway

This project is a Django-based API Gateway that forwards requests to backend services and logs API requests.  It currently integrates with:

- [Weather API](https://github.com/Mehtab-Sidhu/weather-api) (built using FastAPI) 

- [News API](https://newsapi.org/) (third-party integration)

## Features
- Forwards API requests to backend services
- Logs API request and response details
- Fetches weather data from a custom FastAPI Weather API project
- Fetches news data from NewsAPI.org

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Mehtab-Sidhu/api-gateway.git
   cd api-gateway
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

4. Start the Django server:
   ```sh
   python manage.py runserver
   ```

## Usage

### Fetch Weather Data
The API Gateway forwards weather requests to the FastAPI Weather API.
```sh
GET /gateway/weather/?city=Delhi
```

### Fetch News Data
The API Gateway fetches news data from NewsAPI.org.
```sh
GET /gateway/news/?category=technology
```

## API Logging
All requests made through the API Gateway are logged in the `APILog` model, accessible through the Django Admin panel.

## Contribution
Feel free to open issues or submit pull requests to improve this project!

---
Happy coding! 🚀
