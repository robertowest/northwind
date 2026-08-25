"""esquemas de la entidad customer."""

from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    """campos comunes de un cliente."""

    company_name: str
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None


class CustomerCreate(CustomerBase):
    """datos para crear un cliente."""

    customer_id: str


class CustomerUpdate(BaseModel):
    """datos para actualizar un cliente, todos opcionales."""

    company_name: str | None = None
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None


class CustomerRead(CustomerBase):
    """representación de un cliente devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    customer_id: str
