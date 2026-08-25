"""esquemas de la entidad us_state."""

from pydantic import BaseModel, ConfigDict


class UsStateBase(BaseModel):
    """campos comunes de un estado."""

    state_name: str | None = None
    state_abbr: str | None = None
    state_region: str | None = None


class UsStateCreate(UsStateBase):
    """datos para crear un estado."""

    state_id: int


class UsStateUpdate(BaseModel):
    """datos para actualizar un estado."""

    state_name: str | None = None
    state_abbr: str | None = None
    state_region: str | None = None


class UsStateRead(UsStateBase):
    """representación de un estado devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    state_id: int
