from pydantic import BaseModel


class AuthPayload(BaseModel):
    uid: str
    session_id: str


class LoginPayload(BaseModel):
    email: str
    password: str


class LogoutPayload(BaseModel):
    uid: str
    session_id: str


class RegisterPayload(BaseModel):
    email: str
    password: str
