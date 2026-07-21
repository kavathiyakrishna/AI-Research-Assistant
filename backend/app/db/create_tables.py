from backend.app.db.database import engine
from backend.app.db.base import Base

# Import models so SQLAlchemy registers them
from backend.app.models import User


def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()