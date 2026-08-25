"""modelo de la tabla categories."""

from typing import TYPE_CHECKING

from sqlalchemy import LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.product import Product


class Category(Base):
    """categoría a la que pertenecen los productos."""

    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    category_name: Mapped[str] = mapped_column(String(15))
    description: Mapped[str | None] = mapped_column(Text)
    picture: Mapped[bytes | None] = mapped_column(LargeBinary)

    products: Mapped[list['Product']] = relationship(back_populates='category')
