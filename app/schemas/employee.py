"""esquemas de la entidad employee."""

from datetime import date

from pydantic import BaseModel, ConfigDict


class EmployeeBase(BaseModel):
    """campos comunes de un empleado."""

    last_name: str
    first_name: str
    title: str | None = None
    title_of_courtesy: str | None = None
    birth_date: date | None = None
    hire_date: date | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    home_phone: str | None = None
    extension: str | None = None
    notes: str | None = None
    reports_to: int | None = None
    photo_path: str | None = None


class EmployeeCreate(EmployeeBase):
    """datos para crear un empleado."""

    employee_id: int


class EmployeeUpdate(BaseModel):
    """datos para actualizar un empleado, todos opcionales."""

    last_name: str | None = None
    first_name: str | None = None
    title: str | None = None
    title_of_courtesy: str | None = None
    birth_date: date | None = None
    hire_date: date | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    home_phone: str | None = None
    extension: str | None = None
    notes: str | None = None
    reports_to: int | None = None
    photo_path: str | None = None


class EmployeeRead(EmployeeBase):
    """representación de un empleado devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
