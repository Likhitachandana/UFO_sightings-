# UFO Sighting Database Service

This service is a simple REST API built with Flask and SQLAlchemy to track UFO sightings. The API allows you to retrieve sightings by location and date, and it updates its database with new data from the National UFO Reporting Center at least daily.

## Project Structure

├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── sightings.py
│   ├── models
│   │   ├── __init__.py
│   │   └── Sighting.py
│   └── services
│       ├── __init__.py
│       └── scraper.py
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_scraper.py
├── scheduler.py
├── config.py
├── main.py
└── requirements.txt

## Installation

1. Clone this repository: git clone <repository-url>

2. Navigate into the project directory: cd ufo-sighting-database-service

3. Install the required packages: pip install -r requirements.txt

4. Set up the Flask environment variables:

	export FLASK_APP=main.py
	export FLASK_ENV=development
	
## Run the application: flask run

The application will start running at http://127.0.0.1:5000

## Usage

The API currently supports two GET operations:

1. To retrieve all sightings: GET /api/sightings

2. To retrieve sightings by location and/or date: GET /api/sightings?location=<location>&date=<date>

	<location>: The location to filter by (case insensitive).
	<date>: The date to filter by, in the format YYYY-MM-DD.
	
## Testing

The project includes some basic unit tests. You can run them using pytest: pytest