"""base declarativa común para todos los modelos orm."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """clase base de la que heredan todos los modelos sqlalchemy del proyecto."""
