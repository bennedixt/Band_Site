# Band_site

## Overview
Band_site is a Django-based project that serves as the official website for a fictional music band, **Hot Fenix**. The website allows fans to view tour dates, band news, and access exclusive content and stay updated on the band's Grammy achievements.

## Features
- **World Tour Blog**: Display of upcoming tour dates and destinations.
- **User Authentication**: Registered users can log in to access exclusive content.
- **Award Announcements**: Highlights the band's Grammy achievements.
- **Dockerized Deployment**: Run the application in any environment with ease.
- **Sphinx Documentation**: The project includes auto-generated documentation using Sphinx.

## Installation

### Virtual Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Band_site.git
   cd Band_site


2. Create a virtual environment:
   ```bash
   For MacOS/Linux: python3 -m venv venv
   For Windows: python -m venv venv


3. Activate the virtual environment:
   ```bash
   For MacOS/Linux: source venv/bin/activate
   For Windows: venv\Scripts\activate


5. Install dependencies:
   ```bash
   pip install -r requirements.txt


7. Set up the database
   ```bash
   python manage.py migrate


## Docker Setup

To run the project in Docker, follow these steps:

1. Build the Docker image
  Ensure that Docker is installed on your system. Then, build the image by running:
   ```bash
    docker build -t band_site .

  
2. Run the Docker container
  After building the image, run the container with:
   ```bash
    docker run -p 8000:8000 band_site


3. Access the app
  Navigate to http://localhost:8000 in your browser to view the application. 


  ##  Running Tests

  To run the project's tests, use the following command:
    
     python manage.py test


## Documentation

The project includes auto-generated documentation using Sphinx. To view the documentation:

1. Navigate to the docs folder:
   ```bash
   cd docs


2. Build the documentation:
    ```bash
   make html


3. Open the documentation in your browser by navigating to docs/_build/html/index.html.
  

  ## Licence 

  This project is licensed under the MIT License - see the LICENSE file for details.



 







