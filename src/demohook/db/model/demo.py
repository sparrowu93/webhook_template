

from conf.settings import DB_DIR
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_DIR}/eventHooks.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=True, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
     pass

class EventOrm(Base):
    __tablename__ = "event"

    id = Column(String, primary_key=True, nullable=False)
    location = Column(String)
    eventType = Column(String)
    eventName = Column(String)
    startTime = Column(String)
    timestamp = Column(Integer)

class EventHistoryOrm(Base):
    __tablename__ = "event_history"

    id = Column(String, primary_key=True, nullable=False)
    location = Column(String)
    eventType = Column(String)
    eventName = Column(String)
    startTime = Column(String)
    endTime = Column(String)
    startTs = Column(Integer)
    endTs = Column(Integer)