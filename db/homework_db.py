import sqlite3

from db.homework_queries import (
    create_movies_table,
    create_movie_details_table,
    insert_movie,
    insert_movie_detail,
    select_movies
)


DB_NAME = "db/movies.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(create_movies_table)
    cursor.execute(create_movie_details_table)

    conn.commit()
    conn.close()


def add_movie(title, rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        insert_movie,
        (title, rating)
    )

    conn.commit()

    movie_id = cursor.lastrowid

    conn.close()

    return movie_id


def add_movie_detail(movie_id, genre):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        insert_movie_detail,
        (movie_id, genre)
    )

    conn.commit()
    conn.close()


def get_movies():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(select_movies)

    movies = cursor.fetchall()

    conn.close()

    return movies