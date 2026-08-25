"""modelo de la tabla orders."""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.customer import Customer
    from app.models.employee import Employee
    from app.models.order_detail import OrderDetail
    from app.models.shipper import Shipper


class Order(Base):
    """pedido realizado por un cliente."""

    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    customer_id: Mapped[str | None] = mapped_column(String(5), ForeignKey('customers.customer_id'))
    employee_id: Mapped[int | None] = mapped_column(
        SmallInteger, ForeignKey('employees.employee_id')
    )
    order_date: Mapped[date | None] = mapped_column(Date)
    required_date: Mapped[date | None] = mapped_column(Date)
    shipped_date: Mapped[date | None] = mapped_column(Date)
    ship_via: Mapped[int | None] = mapped_column(SmallInteger, ForeignKey('shippers.shipper_id'))
    freight: Mapped[float | None] = mapped_column(Float)
    ship_name: Mapped[str | None] = mapped_column(String(40))
    ship_address: Mapped[str | None] = mapped_column(String(60))
    ship_city: Mapped[str | None] = mapped_column(String(15))
    ship_region: Mapped[str | None] = mapped_column(String(15))
    ship_postal_code: Mapped[str | None] = mapped_column(String(10))
    ship_country: Mapped[str | None] = mapped_column(String(15))

    customer: Mapped['Customer | None'] = relationship(back_populates='orders')
    employee: Mapped['Employee | None'] = relationship(back_populates='orders')
    shipper: Mapped['Shipper | None'] = relationship(back_populates='orders')
    order_details: Mapped[list['OrderDetail']] = relationship(back_populates='order')
