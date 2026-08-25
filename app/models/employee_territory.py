"""modelo de la tabla puente employee_territories (empleados <-> territorios)."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.territory import Territory


class EmployeeTerritory(Base):
    """relación m:n entre employees y territories."""

    __tablename__ = 'employee_territories'

    employee_id: Mapped[int] = mapped_column(
        SmallInteger, ForeignKey('employees.employee_id'), primary_key=True
    )
    territory_id: Mapped[str] = mapped_column(
        String(20), ForeignKey('territories.territory_id'), primary_key=True
    )

    employee: Mapped['Employee'] = relationship(back_populates='territories')
    territory: Mapped['Territory'] = relationship(back_populates='employees')
