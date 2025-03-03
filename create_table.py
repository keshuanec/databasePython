from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

try:
    with connect(host="localhost", user='root', password=password, database="online_movie_rating") as conn:
        # create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"
        movies = """
                CREATE TABLE movies(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(100)
                )
                """
        with conn.cursor() as cursor:
            cursor.execute(movies)
            conn.commit()

except Error as e:
    print(e)


