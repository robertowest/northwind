"""modelo de la tabla employees."""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.employee_territory import EmployeeTerritory
    from app.models.order import Order


class Employee(Base):
    """empleado de la empresa."""

    __tablename__ = 'employees'

    employee_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    last_name: Mapped[str] = mapped_column(String(20))
    first_name: Mapped[str] = mapped_column(String(10))
    title: Mapped[str | None] = mapped_column(String(30))
    title_of_courtesy: Mapped[str | None] = mapped_column(String(25))
    birth_date: Mapped[date | None] = mapped_column(Date)
    hire_date: Mapped[date | None] = mapped_column(Date)
    address: Mapped[str | None] = mapped_column(String(60))
    city: Mapped[str | None] = mapped_column(String(15))
    region: Mapped[str | None] = mapped_column(String(15))
    postal_code: Mapped[str | None] = mapped_column(String(10))
    country: Mapped[str | None] = mapped_column(String(15))
    home_phone: Mapped[str | None] = mapped_column(String(24))
    extension: Mapped[str | None] = mapped_column(String(4))
    photo: Mapped[bytes | None] = mapped_column(LargeBinary)
    notes: Mapped[str | None] = mapped_column(Text)
    reports_to: Mapped[int | None] = mapped_column(
        SmallInteger, ForeignKey('employees.employee_id')
    )
    photo_path: Mapped[str | None] = mapped_column(String(255))

    manager: Mapped['Employee | None'] = relationship(remote_side='Employee.employee_id')
    orders: Mapped[list['Order']] = relationship(back_populates='employee')
    territories: Mapped[list['EmployeeTerritory']] = relationship(back_populates='employee')
