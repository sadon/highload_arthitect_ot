from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
#db_host = 'db'
#db_port = '5432'
db_host = 'localhost'
db_port = '8432'


# Connect to the database
SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL # only for SQLite, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()