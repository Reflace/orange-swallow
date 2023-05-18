import sqlite3


# Название, режиссер, обложка, год, жанр, оценка IMDb, оценка Kinopoisk
def init_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS films (name TEXT NOT NULL, director TEXT NOT NULL,
        picture BLOB NOT NULL, year INT NOT NULL, style TEXT NOT NULL),
        rate_imdb REAL NOT NULL, rate_kinopoisk REAL NOT NULL''')


# Как передать набор значений (4ая строка) в функцию?
def pack_db(*contents):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    init_db(cur)

    insert_blob_query = """INSERT INTO films (name, director, picture, year, style, rate_IMDb, rate_Kinopoisk) 
        VALUES (?, ?, ?, ?, ?, ?, ?)"""

    # for content in contents:
    #     with open(content, 'rb') as f:
    #         blob_data = f.read()
    #     cur.execute(insert_blob_query, (str(content), blob_data))
    # conn.commit()

    cur.close()
    conn.close()
