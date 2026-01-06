from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    university: Literal["University of Porthacourt (UNIPORT)", "Rivers State University (RSU)"]

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    hashed_password: Optional[str] = None

class User(UserBase):
    id: int
    is_verified: bool
    is_student_verified: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserInDB(User):
    hashed_password: str
    otp_code: Optional[str] = None
    otp_expires_at: Optional[datetime] = None

class OTPVerify(BaseModel):
    email: EmailStr
    otp_code: str

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    otp_code: str
    new_password: str
