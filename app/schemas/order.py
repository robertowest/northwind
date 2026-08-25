"""esquemas de la entidad order."""

from datetime import date

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    """campos comunes de un pedido."""

    customer_id: str | None = None
    employee_id: int | None = None
    order_date: date | None = None
    required_date: date | None = None
    shipped_date: date | None = None
    ship_via: int | None = None
    freight: float | None = None
    ship_name: str | None = None
    ship_address: str | None = None
    ship_city: str | None = None
    ship_region: str | None = None
    ship_postal_code: str | None = None
    ship_country: str | None = None


class OrderCreate(OrderBase):
    """datos para crear un pedido."""

    order_id: int


class OrderUpdate(BaseModel):
    """datos para actualizar un pedido, todos opcionales."""

    customer_id: str | None = None
    employee_id: int | None = None
    order_date: date | None = None
    required_date: date | None = None
    shipped_date: date | None = None
    ship_via: int | None = None
    freight: float | None = None
    ship_name: str | None = None
    ship_address: str | None = None
    ship_city: str | None = None
    ship_region: str | None = None
    ship_postal_code: str | None = None
    ship_country: str | None = None


class OrderRead(OrderBase):
    """representación de un pedido devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    order_id: int
