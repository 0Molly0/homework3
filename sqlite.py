import sqlite3

with sqlite3.connect('new_tables.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    query = """
        CREATE TABLE IF NOT EXISTS author(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            authors TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            book TEXT NOT NULL,
            number_of_pages INTEGER CHECK (number_of_pages > 0),
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES author(id)
        )
    """
    cursor.executescript(query)

    values = ['Стівен Кінг'], ['Олександр Авраменко'], ['Оксана Карпюк']

    query = """
        INSERT INTO author(authors)
        VALUES (?)
    """
    cursor.executemany(query, values)

    values = (
        ('Кладовище домашніх тварин', 397, 1),
        ('Українська література', 335, 2),
        ('Англійська мова', 287, 3)
    )

    query = """
        INSERT INTO book(book, number_of_pages, author_id)
        VALUES (?, ?, ?)
    """
    cursor.executemany(query, values)

    query = """
        SELECT book, authors, number_of_pages, author_id, book.id
        FROM book
        JOIN author
        ON book.author_id = author.id
    """
    result = cursor.execute(query)
    print(result.fetchall())

    query = """
        SELECT book, authors, number_of_pages, author_id, book.id
        FROM book
        LEFT JOIN author
        ON book.author_id = author.id
    """
    result = cursor.execute(query)
    print(result.fetchall())

    query = """
        SELECT book, authors, number_of_pages, author_id, book.id
        FROM author
        FULL JOIN book
        ON book.author_id = author.id
    """
    result = cursor.execute(query)
    print(result.fetchall())
