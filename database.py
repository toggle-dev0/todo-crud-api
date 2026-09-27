from collections.abc import Generator
from pathlib import Path
from sqlmodel import SQLModel, Session, create_engine
from models.task import Task

sqlite_file_name = "database.db"
# Use 'sqlite:///' for a local file database
sqlite_url = f"sqlite:///{sqlite_file_name}"

# connect_args={"check_same_thread": False} is ONLY needed for SQLite
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """Create the database and seed starter tasks on first initialization."""
    is_first_initialization = not Path(sqlite_file_name).exists()
    SQLModel.metadata.create_all(engine)

    if is_first_initialization:
        with Session(engine) as session:
            session.add_all(
                [
                    Task(title="Learn FastAPI"),
                    Task(title="Build a todo API"),
                    Task(title="Explore SQLite"),
                ]
            )
            session.commit()


def get_session() -> Generator[Session, None, None]:
    """Dependency provider for database sessions."""
    with Session(engine) as session:
        yield session