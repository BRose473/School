The goal of this project is to build an ETL pipeline that collects book metadata from the Google Books API, cleans and standardizes the data, stores it in a relational database, and enables SQL-based analysis of genres, authors, publishers, and publication trends. 

To start, I know I don't want to download everything the API returns, but only for Books: Google Books ID, ISBN-10, ISBN-13, Title, Subtitle, Description, Page Count, Language, Published Date, and Publisher; Author: Name (will include Author ID in database); Categories (Genres); Format (may not need as all may be ebooks); Ratings: Average Rating and Rating Count. 

To avoid duplicated data the database will be set up as follows: 

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
