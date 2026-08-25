"""modelo de la tabla products."""

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.order_detail import OrderDetail
    from app.models.supplier import Supplier


class Product(Base):
    """producto que se comercializa."""

    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    product_name: Mapped[str] = mapped_column(String(40))
    supplier_id: Mapped[int | None] = mapped_column(
        SmallInteger, ForeignKey('suppliers.supplier_id')
    )
    category_id: Mapped[int | None] = mapped_column(
        SmallInteger, ForeignKey('categories.category_id')
    )
    quantity_per_unit: Mapped[str | None] = mapped_column(String(20))
    unit_price: Mapped[float | None] = mapped_column(Float)
    units_in_stock: Mapped[int | None] = mapped_column(SmallInteger)
    units_on_order: Mapped[int | None] = mapped_column(SmallInteger)
    reorder_level: Mapped[int | None] = mapped_column(SmallInteger)
    discontinued: Mapped[int] = mapped_column(Integer)

    supplier: Mapped['Supplier | None'] = relationship(back_populates='products')
    category: Mapped['Category | None'] = relationship(back_populates='products')
    order_details: Mapped[list['OrderDetail']] = relationship(back_populates='product')
