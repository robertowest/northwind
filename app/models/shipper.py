"""modelo de la tabla shippers."""

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.order import Order


class Shipper(Base):
    """empresa transportista que sirve los pedidos."""

    __tablename__ = 'shippers'

    shipper_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    company_name: Mapped[str] = mapped_column(String(40))
    phone: Mapped[str | None] = mapped_column(String(24))

    orders: Mapped[list['Order']] = relationship(back_populates='shipper')
