"""
Zavedeme do databáze vztahy one-to-many (jeden k mnoha):

jeden vůz -> mnoho rezervací, jedna rezervace -> jeden vůz
jeden klient -> mnoho rezervací, jedna rezervace -> jeden klient
Do tříd Clients, Cars, Bookings přidáme potřebný kód, který je propojí s uvedenými vztahy.
Vztahy by měly být obousměrné - od úrovně instance Cars bychom měli přistupovat k instanci
Booking prostřednictvím vlastnosti bookings. Podobně pro instanci třídy Clients. Dále je vhodné zkontrolovat
chování při mazání souvisejících záznamů. Nakonec bychom chtěli aktualizovat tabulku bookings. když odstraníme
záznam z tabulky klienti nebo automobily. Implementujte výše zmíněné.
"""

from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

eng = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/car_rental')

base = declarative_base()

from sqlalchemy.orm import relationship


class Cars(base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)
    bookings = relationship('Bookings', back_populates='car', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"<Car: id={self.car_id}, producer={self.producer}, model={self.model}, year={self.year}, "
        f"horse_power={self.horse_power}, price_per_day={self.price_per_day}>"


class Clients(base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    bookings = relationship('Bookings', back_populates='client', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"<Client: id={self.client_id}, name={self.name}, surname={self.surname}, address={self.address},"
        f"city={self.city}>"


class Bookings(base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.client_id', ondelete="CASCADE"), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.car_id', ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    client = relationship('Clients', back_populates='bookings')
    car = relationship('Cars', back_populates='bookings')

    def __repr__(self):
        return f"<Booking: id={self.booking_id}, client_id={self.client_id}, car_id={self.car_id}, start_date={self.start_date}, end_date={self.end_date}, total_amount={self.total_amount}>"
