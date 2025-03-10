"""insert 3 klienty

pomoci DESCRIBE clients si prohlidnu tabulku
('client_id', 'int', 'NO', 'PRI', None, 'auto_increment'),
('name', 'varchar(30)', 'NO', '', None, ''),
('surname', 'varchar(30)', 'NO', '', None, ''),
('address', 'varchar(30)', 'NO', '', None, ''),
('city', 'varchar(30)', 'NO', '', None, '')]

"""


from mysql.connector import connect

with open("moje_heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password, database="car_rental") as conn:
    with conn.cursor() as cursor:
        data = [
            {"name": "Francek", "surname": "Plundra", "address": "Prdelakov 321", "city": "dira"},
            {"name": "Lojzek", "surname": "Turna", "address": "Prdelnikov 456", "city": "dira"},
        ]

        cursor.executemany(
            """
            INSERT INTO clients (name, surname, address, city)
            VALUES (%(name)s, %(surname)s, %(address)s, %(city)s)
            """, data)


        conn.commit()

        print("insert probehl spravne")