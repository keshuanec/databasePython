from mysql.connector import connect, Error

with open("moje_heslo.txt", 'r') as file:
    password = file.read()
try:
    with connect(host="localhost", user='root', password=password, database="music") as conn:
        create_database = """
        CREATE DATABASE IF NOT EXISTS music;
        """
        create_tables = """
        CREATE TABLE instruments(
                    instrument_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    family VARCHAR(100),
                    dificulty ENUM("easy","medium", "hard") NOT NULL);
        """

        with conn.cursor() as cursor:
            cursor.execute(create_database)
            cursor.execute(create_tables)



except Error as e:(
    print(e))