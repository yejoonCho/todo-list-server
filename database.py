from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///task.db')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


