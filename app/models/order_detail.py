"""modelo de la tabla puente order_details (líneas de pedido, pedidos <-> productos)."""

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.order import Order
    from app.models.product import Product


class OrderDetail(Base):
    """línea de un pedido: relación m:n entre orders y products con datos propios."""

    __tablename__ = 'order_details'

    order_id: Mapped[int] = mapped_column(
        SmallInteger, ForeignKey('orders.order_id'), primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        SmallInteger, ForeignKey('products.product_id'), primary_key=True
    )
    unit_price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(SmallInteger)
    discount: Mapped[float] = mapped_column(Float)

    order: Mapped['Order'] = relationship(back_populates='order_details')
    product: Mapped['Product'] = relationship(back_populates='order_details')
