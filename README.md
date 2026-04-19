CYPTO_WEATHER

This project is a multi-source ETL (Extract, Transform, Load) data pipeline built using Python. It collects real-time data from external APIs, processes it, and stores it in a relational database.

The pipeline integrates:

>Cryptocurrency prices (Bitcoin, Ethereum)
>Weather data (Johannesburg)
>Architecture

ETL Flow:

Extract
Fetch crypto data from CoinGecko API
Fetch weather data from Open-Meteo API
Transform
Clean and structure data using Pandas
Add timestamps for tracking historical trends
Load
Store data in a SQLite database
Use SQLAlchemy ORM for database interaction
> Tech Stack
Python
Pandas
SQLAlchemy
SQLite
Requests
