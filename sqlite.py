import sqlite3

with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS books(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name TEXT NOT NULL,
    #         number_of_pages INTEGER CHECK (number_of_pages > 0),
    #         price DECIMAL(10, 2) CHECK (price > 0)
    #     )
    # """
    # cursor.execute(query)

    # name = 'Гра престолів'
    # number_of_pages = 800
    # price = 775
    # values = [name, number_of_pages, price]
    #
    # query = """
    #     INSERT INTO books(name, number_of_pages, price)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # values = (
    #     ('Біологія', 234, 369),
    #     ('Кладовище домашніх тварин', 397, 327),
    #     ('Пташині збори', 328, 232),
    #     ('Українська література', 335, 300),
    #     ('Історія України', 287, 99),
    #     ('Всесвітня історія', 256, 50)
    # )
    #
    # query = """
    #     INSERT INTO books(name, number_of_pages, price)
    #     VALUES (?, ?, ?)
    # """
    # cursor.executemany(query, values)

    query = """
        SELECT name, number_of_pages, price
        FROM books
        WHERE price > 100
    """

    result = cursor.execute(query)
    print(result.fetchall())

    query = """
        SELECT name, number_of_pages, price
        FROM books
        ORDER BY price ASC
        LIMIT 3
    """

    result = cursor.execute(query)
    print(result.fetchall())

    query = """
        SELECT name, number_of_pages, price
        FROM books
        WHERE name LIKE '%сторія%'
        LIMIT 2
    """

    result = cursor.execute(query)
    print(result.fetchall())

    # query = """
    #     ALTER TABLE books
    #     ADD COLUMN barcode TEXT
    # """
    #
    # cursor.execute(query)

    # query = """
    #     UPDATE books
    #     SET barcode = '0-00045'
    #     WHERE number_of_pages > 300
    # """
    # cursor.execute(query)

    # query = """
    #     DELETE FROM books
    #     WHERE price = 300
    # """
    # cursor.execute(query)
