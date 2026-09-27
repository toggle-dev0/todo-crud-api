from collections.abc import Generator
from sqlmodel import SQLModel, Session, create_engine
# from models.task import task_instances as instances

sqlite_file_name = "database.db"
# Use 'sqlite:///' for a local file database
sqlite_url = f"sqlite:///{sqlite_file_name}"

# connect_args={"check_same_thread": False} is ONLY needed for SQLite
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)

# def set_seed():
#     with Session(engine) as session:
#         for item in instances:
#             session.add(item)
#         session.commit()

def get_session() -> Generator[Session, None, None]:
    """Dependency provider for database sessions."""
    with Session(engine) as session:
        yield session