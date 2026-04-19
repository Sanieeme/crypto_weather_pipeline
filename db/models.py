from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True)
    coin = Column(String)
    price = Column(Float)
    timestamp = Column(DateTime)


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    windspeed = Column(Float)
    timestamp = Column(DateTime)