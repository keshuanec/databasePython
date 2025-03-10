from mysql.connector import connect


with open('moje_heslo.txt', 'r') as file:
    password = file.read()

with connect(host = 'localhost', user='root', password=password) as conn:
    test_sellect = "SELECT 1"
    with conn.cursor() as cursor:
        cursor.execute(test_sellect)
        print(cursor.fetchall())

