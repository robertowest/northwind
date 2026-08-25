"""esquemas de la entidad puente customer_customer_demo."""

from pydantic import BaseModel, ConfigDict


class CustomerCustomerDemoCreate(BaseModel):
    """datos para asociar un cliente a un perfil demográfico."""

    customer_id: str
    customer_type_id: str


class CustomerCustomerDemoRead(BaseModel):
    """representación de la asociación cliente <-> perfil demográfico."""

    model_config = ConfigDict(from_attributes=True)

    customer_id: str
    customer_type_id: str
