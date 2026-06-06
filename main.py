from fastapi import FastAPI
from pydantic import BaseModel

from database import engine
from database import SessionLocal
from database import Base

import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class WebsiteCreate(BaseModel):
    website: str

class FocusCreate(BaseModel):
    status: str    


@app.get("/")
def home():
    return {"message": "Backend Working"}


@app.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered Successfully"}


@app.post("/login")
def login(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
    ).first()

    if existing_user:
        return {"message": "Login Successful"}

    return {"message": "Invalid Email or Password"}


@app.post("/add-website")
def add_website(data: WebsiteCreate):

    db = SessionLocal()

    website = models.BlockedWebsite(
        website=data.website
    )

    db.add(website)
    db.commit()

    return {"message": "Website Added Successfully"}

@app.post("/start-focus")
def start_focus(data: FocusCreate):

    db = SessionLocal()

    session = models.FocusSession(
        status=data.status
    )

    db.add(session)
    db.commit()

    return {"message": "Focus Session Started"}    

@app.get("/users")
def get_users():

    db = SessionLocal()

    users = db.query(models.User).all()

    return users


@app.get("/websites")
def get_websites():

    db = SessionLocal()

    websites = db.query(models.BlockedWebsite).all()

    return websites


@app.get("/focus-sessions")
def get_focus_sessions():

    db = SessionLocal()

    sessions = db.query(models.FocusSession).all()

    return sessions    