"""modelo de la tabla customer_demographics."""

from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.customer_customer_demo import CustomerCustomerDemo


class CustomerDemographic(Base):
    """perfil demográfico que puede asociarse a varios clientes."""

    __tablename__ = 'customer_demographics'

    customer_type_id: Mapped[str] = mapped_column(String(5), primary_key=True)
    customer_desc: Mapped[str | None] = mapped_column(Text)

    customers: Mapped[list['CustomerCustomerDemo']] = relationship(back_populates='demographic')
