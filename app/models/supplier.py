"""modelo de la tabla suppliers."""

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.product import Product


class Supplier(Base):
    """proveedor que suministra productos."""

    __tablename__ = 'suppliers'

    supplier_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    company_name: Mapped[str] = mapped_column(String(40))
    contact_name: Mapped[str | None] = mapped_column(String(30))
    contact_title: Mapped[str | None] = mapped_column(String(30))
    address: Mapped[str | None] = mapped_column(String(60))
    city: Mapped[str | None] = mapped_column(String(15))
    region: Mapped[str | None] = mapped_column(String(15))
    postal_code: Mapped[str | None] = mapped_column(String(10))
    country: Mapped[str | None] = mapped_column(String(15))
    phone: Mapped[str | None] = mapped_column(String(24))
    fax: Mapped[str | None] = mapped_column(String(24))
    homepage: Mapped[str | None] = mapped_column(Text)

    products: Mapped[list['Product']] = relationship(back_populates='supplier')
