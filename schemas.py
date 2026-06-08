from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class WebsiteCreate(BaseModel):
    website: str
    user_id: int


class FocusCreate(BaseModel):
    status: str
    user_id: int
