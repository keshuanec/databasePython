from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum
from sqlalchemy.orm import sessionmaker

with open("moje_heslo.txt", 'r') as file:
    password = file.read()
db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/online_movie_rating')


Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))


    def __repr__(self):
        return self.title


movies = session.query(Movie).all()

print(movies)