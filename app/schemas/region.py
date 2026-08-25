"""esquemas de la entidad region."""

from pydantic import BaseModel, ConfigDict


class RegionBase(BaseModel):
    """campos comunes de una región."""

    region_description: str


class RegionCreate(RegionBase):
    """datos para crear una región."""

    region_id: int


class RegionUpdate(BaseModel):
    """datos para actualizar una región."""

    region_description: str | None = None


class RegionRead(RegionBase):
    """representación de una región devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    region_id: int
