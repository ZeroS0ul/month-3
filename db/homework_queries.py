create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        rating REAL NOT NULL
    )
"""


create_movie_details_table = """
    CREATE TABLE IF NOT EXISTS movie_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
"""


insert_movie = """
    INSERT INTO movies (title, rating)
    VALUES (?, ?)
"""


insert_movie_detail = """
    INSERT INTO movie_details (movie_id, genre)
    VALUES (?, ?)
"""


select_movies = """
    SELECT
        movies.id,
        movies.title,
        movie_details.genre,
        movies.rating
    FROM movies
    INNER JOIN movie_details
        ON movies.id = movie_details.movie_id
"""

