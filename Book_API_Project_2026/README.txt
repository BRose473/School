A Python-based ETL (Extract, Transform, Load) pipeline that retrieves book metadata from the Google Books API, cleans and standardizes the data, loads it into a PostgreSQL database, and enables SQL-based analysis of authors, publishers, categories, and publication trends.

This project demonstrates API integration, data modeling, ETL development, SQL, and data quality handling using real-world book metadata.
----------------------------------------------------------------------------------------------------------------------------

The goal of this project is to build an ETL pipeline that collects book metadata from the Google Books API, cleans and standardizes the data, stores it in a relational database, and enables SQL-based analysis of genres, authors, publishers, and publication trends. 

To start, I know I don't want to download everything the API returns, but only for Books: Google Books ID, ISBN-10, ISBN-13, Title, Subtitle, Description, Page Count, Language, Published Date, and Publisher; Author: Name (will include Author ID in database); Categories (Genres); Format (may not need as all may be ebooks); Ratings: Average Rating and Rating Count. 


Technologies
----------------------------------------------------------------------------------------
- Python
- Google Books API
- PostgreSQL
- SQL
- requests
- python-dotenv
- Git 


Database Schema
----------------------------------------------------------------------------------------------------------------------------
Books
------
book_id (PK)
google_book_id
title
subtitle
description
page_count
language
publisher_id (FK)
published_date
average_rating
ratings_count

Authors
------
author_id (PK)
author_name

BookAuthors
------
book_id (PK FK)
author_id (PK FK)

Publishers
------
publisher_id (PK)
publisher_name

Categories
------
category_id (PK)
category_name

BookCategories
------
book_id (PK FK)
category_id (PK FK)


Data Cleaning & Transformation Rules
-------------------------------------------------------------------------------------------------------------------------
Duplicate Books                Skip duplicate Google Books IDs
Missing ISBN                   Store as NULL
Missing Author                 Store as Unknown Author 
Multiple Authors               Store each author separately in the Authors table and create entries in BookAuthors
Multiple Categories            Store each category separately and create entries in Book Categories
Missing Publisher              Store as NULL
Invalid Publication Date       Attempt to parse; if unsuccessful, store as NULL
Empty Descriptions             Store as NULL
Leading/trailing whitespace    Trim before loading
Duplicate Categories           Reuse existing category records rather than creating duplicates


Data Pipeline
------------------------------------------------------------------------------------------------------------------------
Google Books API
        │
        ▼
Extract Raw JSON
        │
        ▼
Validate Response
        │
        ▼
Clean & Standardize Data
        │
        ▼
Load into PostgreSQL
        │
        ▼
SQL Analysis


Future Enhancements
----------------------------------------------------------------------------------------------------------------------
Incremental ETL updates (only load new books)

Automated scheduled pipeline

Docker support

Cloud Storage for raw JSON

Data quality reporting

Analytics Dashboard

Unit tests and CI/CD