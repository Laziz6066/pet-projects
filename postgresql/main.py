import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f'Server version: {cursor.fetchone()}')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         nick_name varchar(50) NOT NULL);"""
    #     )
    #
    #     print("[INFO] Table created successfully")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Lazik', 'Smash');"""
    #     )
    #     print('[INFO] Data was successfully inserted')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Lazik';"""
    #     )
    #     print(cursor.fetchone())

    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        print('[INFO] Table was deleted')

except Exception as ex:
    print('[INFO] Error while working with PostgreSQL:', ex)  # Print the actual error message
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')

