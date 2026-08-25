"""esquemas de la entidad customer_demographic."""

from pydantic import BaseModel, ConfigDict


class CustomerDemographicBase(BaseModel):
    """campos comunes de un perfil demográfico."""

    customer_desc: str | None = None


class CustomerDemographicCreate(CustomerDemographicBase):
    """datos para crear un perfil demográfico."""

    customer_type_id: str


class CustomerDemographicUpdate(BaseModel):
    """datos para actualizar un perfil demográfico."""

    customer_desc: str | None = None


class CustomerDemographicRead(CustomerDemographicBase):
    """representación de un perfil demográfico devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    customer_type_id: str
