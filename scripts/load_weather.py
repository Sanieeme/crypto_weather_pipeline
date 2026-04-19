from sqlalchemy.orm import sessionmaker
from db.db_connection import engine
from db.models import WeatherData

Session = sessionmaker(bind=engine)

def load_weather(df):
    session = Session()

    for _, row in df.iterrows():
        record = WeatherData(
            temperature=row["temperature"],
            windspeed=row["windspeed"],
            timestamp=row["timestamp"]
        )
        session.add(record)

    session.commit()
    session.close()