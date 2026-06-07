from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str  # Make sure to hash this later

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class WebsiteCreate(BaseModel):
    website: str

class FocusCreate(BaseModel):
    status: str  # For example, "ACTIVE"
