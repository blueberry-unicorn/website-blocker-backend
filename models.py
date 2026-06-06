from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class BlockedWebsite(Base):
    __tablename__ = "blocked_websites"

    id = Column(Integer, primary_key=True, index=True)
    website = Column(String)

class FocusSession(Base):
    __tablename__ = "focus_sessions"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)    