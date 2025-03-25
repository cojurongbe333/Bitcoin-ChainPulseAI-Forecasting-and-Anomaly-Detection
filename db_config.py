
from sqlalchemy import create_engine

# Update this URL with your actual database credentials
DATABASE_URL = "postgresql://username:password@localhost:5432/chainpulse"

engine = create_engine(DATABASE_URL)
