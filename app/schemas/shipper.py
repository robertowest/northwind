"""esquemas de la entidad shipper."""

from pydantic import BaseModel, ConfigDict


class ShipperBase(BaseModel):
    """campos comunes de un transportista."""

    company_name: str
    phone: str | None = None


class ShipperCreate(ShipperBase):
    """datos para crear un transportista."""

    shipper_id: int


class ShipperUpdate(BaseModel):
    """datos para actualizar un transportista."""

    company_name: str | None = None
    phone: str | None = None


class ShipperRead(ShipperBase):
    """representación de un transportista devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    shipper_id: int
