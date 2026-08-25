import sqlite3

from db.homework_queries import (
    create_movies_table,
    insert_movie,
    select_movies
)

DB_NAME = "db/movies.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(create_movies_table)

    conn.commit()
    conn.close()


def add_movie(title, genre, rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        insert_movie,
        (title, genre, rating)
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