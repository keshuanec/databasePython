"""
Napište funkci insert_instruments, která bude zodpovědná za doplnění údajů do tabulky nástrojů.
 Funkce by měla přijímat dva argumenty - připojení k databázi a seznam záznamů, které se mají vložit.
  Otestujte funkci na následujícím seznamu:
  instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')]

"""

from mysql.connector import connect

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

conn = connect(host="localhost", user='root', password=password, database="music")
instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')]

def instrument_insert(conn, instruments):
    cursor = conn.cursor()
    insert_sql = """ INSERT INTO instruments (name, family, difficulty)
    VALUES(%s, %s, %s)
    """
    cursor.executemany(insert_sql, instruments)
    conn.commit()

instrument_insert(conn, instruments)