from sqlalchemy.ext.asyncio import AsyncSession
from db.models.user import User
from sqlalchemy import select

async def get_user_by_email(db: AsyncSession, email: str):
    stmt = select(User).where(User.email == email)
    return db.session.scalars(stmt).first()