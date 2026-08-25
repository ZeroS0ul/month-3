create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        rating REAL NOT NULL
    )
"""

insert_movie = """
    INSERT INTO movies (title, genre, rating)
    VALUES (?, ?, ?)
"""

select_movies = """
    SELECT id, title, genre, rating
    FROM movies
"""