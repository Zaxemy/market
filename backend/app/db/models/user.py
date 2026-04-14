
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    hashed_password: Mapped[str] = mapped_column("password", String(255), nullable=False)