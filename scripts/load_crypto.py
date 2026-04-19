from sqlalchemy.orm import sessionmaker
from db.db_connection import engine
from db.models import CryptoPrice

Session = sessionmaker(bind=engine)

def load_crypto(df):
    session = Session()

    for _, row in df.iterrows():
        record = CryptoPrice(
            coin=row["coin"],
            price=row["price"],
            timestamp=row["timestamp"]
        )
        session.add(record)

    session.commit()
    session.close()