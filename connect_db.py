from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example7.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
