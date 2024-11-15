# Band_site

## Setup with Virtual Environment
1. Create a virtual environment: `python -m venv venv`
2. Activate it (macOS): `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python manage.py runserver`

## Setup with Docker
1. Build Docker image: `docker build -t band_site .`
2. Run the container: `docker run -p 8000:8000 band_site`

## Environment Variables
Add any environment variables (like secret keys) manually to a `.env` file, and update `.gitignore` to exclude this file.
