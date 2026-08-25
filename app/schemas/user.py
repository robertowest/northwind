"""esquemas del modelo User."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """campos comunes de usuario."""

    username: str


class UserCreate(UserBase):
    """datos necesarios para registrar un usuario."""

    password: str


class UserRead(UserBase):
    """representación de usuario devuelta por la api (nunca incluye la contraseña)."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    created_at: datetime
