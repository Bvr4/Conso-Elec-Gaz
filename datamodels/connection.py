"""Database Connection class."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .sql_models import Base

class DatabaseConnection:
    """Database connection class."""

    def __init__(self):
        """Set up database connection."""
        self.engine = create_engine("sqlite:///database.sqlite")
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        """Get sqlalchemy session."""
        return self.Session()
    