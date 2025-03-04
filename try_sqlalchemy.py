from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("moje_heslo.txt", 'r') as file:
    password = file.read()
db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/online_movie_rating')

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()

#select
result = session.execute(text("SELECT * FROM movies"))
rows = result.fetchall()
for row in rows:
    print(row)