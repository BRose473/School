CREATE TABLE Publishers (
	publisher_id SERIAL PRIMARY KEY,
	publisher_name TEXT
)

CREATE TABLE Books (
	book_id SERIAL PRIMARY KEY,
	google_book_id TEXT,
	isbn_10 TEXT, 
	isbn_13 TEXT,
	title TEXT,
	subtitle TEXT,
	description TEXT,
	page_count SMALLINT,
	lang TEXT,
	publisher_id INT REFERENCES publishers(publisher_id),
	published_date DATE,
	average_rating SMALLINT,
	ratings_count INT
)

CREATE TABLE Authors (
	author_id SERIAL PRIMARY KEY,
	author_name TEXT
)

CREATE TABLE BookAuthors (
	book_id INT REFERENCES Books(book_id),
	author_id INT REFERENCES Authors(author_id)
)