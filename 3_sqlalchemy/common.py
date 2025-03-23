from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(
    url="sqlite:///example.db",
    echo=True
)

session_factory = sessionmaker(
    bind=engine
)

Base = declarative_base()
