"""esquemas de la entidad territory."""

from pydantic import BaseModel, ConfigDict


class TerritoryBase(BaseModel):
    """campos comunes de un territorio."""

    territory_description: str
    region_id: int


class TerritoryCreate(TerritoryBase):
    """datos para crear un territorio."""

    territory_id: str


class TerritoryUpdate(BaseModel):
    """datos para actualizar un territorio."""

    territory_description: str | None = None
    region_id: int | None = None


class TerritoryRead(TerritoryBase):
    """representación de un territorio devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    territory_id: str
