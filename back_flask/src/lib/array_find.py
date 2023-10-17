import json
import psycopg2
from psycopg2 import Error
from password import DB_CONNECT

try:
    connection = psycopg2.connect(
        user=DB_CONNECT.get("user"),
        password=DB_CONNECT.get("password"),
        host=DB_CONNECT.get("host"),
        port=DB_CONNECT.get("port"),
        database=DB_CONNECT.get("database")
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pytable")
    post = cursor.fetchall()
    print(post)


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
