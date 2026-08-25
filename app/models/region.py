"""modelo de la tabla region."""

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.territory import Territory


class Region(Base):
    """región geográfica a la que pertenecen los territorios."""

    __tablename__ = 'region'

    region_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    region_description: Mapped[str] = mapped_column(String(60))

    territories: Mapped[list['Territory']] = relationship(back_populates='region')
