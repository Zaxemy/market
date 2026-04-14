import datetime
import jwt
from passlib.context import CryptContext
from core.config import settings



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + datetime.timedelta(minutes=settings.jwt_auth.LIFETIME_SECONDS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt_auth.SECRET, algorithm=settings.jwt_auth.ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(token, settings.jwt_auth.SECRET , algorithms=[settings.jwt_auth.ALGORITHM])
    except:
        return None