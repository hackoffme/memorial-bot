from pydantic import BaseModel, EmailStr, constr, validator


class UserBase(BaseModel):
    email: EmailStr
    is_active: bool
    is_admin: bool


class UserIn(UserBase):
    password: constr(min_length=8)
    password2: str
    @validator('password2')
    def pass_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Password do not match')
        return v
    class Config:
        orm_mode = True


class User(UserBase):
    id: int = None
    hashed_password: str = None
    class Config:
        orm_mode = True
