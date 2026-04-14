from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.core.security import create_access_token, hash_password, verify_password
from backend.app.db.models.user import User
from db.models.db_helper import db_helper
from dependencies.auth import get_user_by_email
from core.config import settings

router = APIRouter()

@router.post("/register")
async def register(email: str, password: str, db: AsyncSession = Depends(db_helper.get_db)):
    user = get_user_by_email(db, email)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User created"}


@router.post("/login")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(db_helper.get_db)):
    user = get_user_by_email(db, form_data.email)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})

    response.set_cookie(
        key=settings.jwt_auth.SECRET,
        value=token,
        httponly=True,
        secure=False,  
        samesite="lax"
    )

    return {"msg": "Logged in"}


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"msg": "Logged out"}
