from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these with your actual MySQL database credentials
DATABASE_URL = "mysql+pymysql://your_username:your_password@localhost:3306/twitter_clone_db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a session for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for creating database models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
