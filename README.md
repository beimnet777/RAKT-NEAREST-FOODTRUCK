# RAKT-NEAREST-FOODTRUCK
# Nearest Food Trucks Finder

A Django-based web application to find and display the nearest food trucks based on user-provided latitude and longitude coordinates. This project includes an API for accessing data and a small user-friendly frontend to interact with the service.

---

## Features
- RESTful API to query nearby food trucks.
- Interactive frontend templates to input and display results.
- Pagination for listing food trucks.
- Dynamic validation for latitude and longitude inputs.
- Hosted live on Render for easy access.

---

## Table of Contents
1. [Live Demo](#live-demo)
2. [Implementation](#Implementation)
3. [License](#license)
4. [Contact](#Contact)

---

## Live Demo
Visit the deployed version of the app:  
[Nearest Food Trucks Finder](https://rakt-nearest-foodtruck-challenge.onrender.com/foodtrucksnearby/)

---
## Implementation
### Overview
This project is designed to help users find the nearest food trucks based on their current location. The core functionality is built using Django and MongoDB, with RESTful APIs to handle the backend logic and a simple template interface for front-end interaction.

### Key features include:

Location-based querying of food trucks near the user.
A simple interface to interact with the API and view food trucks' details.
A command to populate the database with sample data for development purposes.

### Backend
The backend is powered by Django, which handles the web framework and serves APIs. MongoDB is used as the database to store the food truck data.

### Geospatial Indexing in MongoDB for Nearest Location Queries
The 2dsphere index was used to enable efficient geospatial queries for finding the nearest food trucks based on latitude and longitude. By indexing the location field, MongoDB can perform proximity searches using the $nearSphere operator, which calculates distances using spherical geometry.

This approach is highly efficient as it allows MongoDB to quickly filter and return the nearest food trucks, even with large datasets, by leveraging the optimized geospatial index. Using this indexing method reduces computational complexity and significantly speeds up the search process. The decision to use MongoDB's geospatial indexing was driven by the need for fast, scalable, and accurate location-based queries, making it an ideal solution for the food truck location system.

### Database Population:

A custom management command is created to populate the database with sample food truck data.
### Frontend
A basic HTML interface is provided for users to interact with the API. It includes forms for entering the latitude and longitude coordinates to find nearby food trucks.
---
## Liscence

The Challange is a challange by RAKT Technologies. The implementation is fully done by Beimnet Bekele Guta.///
---
## Contact

For any question Please reach out to me at beimnetbekele123@gmail.com
