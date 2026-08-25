"""modelo de la tabla customers."""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.customer_customer_demo import CustomerCustomerDemo
    from app.models.order import Order


class Customer(Base):
    """cliente que realiza pedidos."""

    __tablename__ = 'customers'

    customer_id: Mapped[str] = mapped_column(String(5), primary_key=True)
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

    orders: Mapped[list['Order']] = relationship(back_populates='customer')
    demographics: Mapped[list['CustomerCustomerDemo']] = relationship(back_populates='customer')
