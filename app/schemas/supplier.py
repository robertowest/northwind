"""esquemas de la entidad supplier."""

from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    """campos comunes de un proveedor."""

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
    homepage: str | None = None


class SupplierCreate(SupplierBase):
    """datos para crear un proveedor."""

    supplier_id: int


class SupplierUpdate(BaseModel):
    """datos para actualizar un proveedor, todos opcionales."""

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
    homepage: str | None = None


class SupplierRead(SupplierBase):
    """representación de un proveedor devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    supplier_id: int
