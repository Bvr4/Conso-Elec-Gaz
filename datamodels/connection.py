"""Database Connection class."""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .sql_models import Base

class DatabaseConnection:
    """Database connection class."""

    def __init__(self):
        """Set up database connection."""
        self.engine = create_engine("sqlite:///database.sqlite")
            
        # Enable spatialite extension for sqlite db
        @event.listens_for(self.engine, 'connect')
        def load_spatialite(dbapi_conn, connection_record):
            dbapi_conn.enable_load_extension(True)
            dbapi_conn.execute('SELECT load_extension("mod_spatialite")')
            dbapi_conn.enable_load_extension(False)

        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        """Get sqlalchemy session."""
        return self.Session()
       