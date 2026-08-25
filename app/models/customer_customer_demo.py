"""modelo de la tabla puente customer_customer_demo (clientes <-> perfiles demográficos)."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.customer import Customer
    from app.models.customer_demographic import CustomerDemographic


class CustomerCustomerDemo(Base):
    """relación m:n entre customers y customer_demographics."""

    __tablename__ = 'customer_customer_demo'

    customer_id: Mapped[str] = mapped_column(
        String(5), ForeignKey('customers.customer_id'), primary_key=True
    )
    customer_type_id: Mapped[str] = mapped_column(
        String(5), ForeignKey('customer_demographics.customer_type_id'), primary_key=True
    )

    customer: Mapped['Customer'] = relationship(back_populates='demographics')
    demographic: Mapped['CustomerDemographic'] = relationship(back_populates='customers')
