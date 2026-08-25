"""esquemas de la entidad puente order_detail (líneas de pedido)."""

from pydantic import BaseModel, ConfigDict


class OrderDetailBase(BaseModel):
    """campos comunes de una línea de pedido."""

    unit_price: float
    quantity: int
    discount: float = 0.0


class OrderDetailCreate(OrderDetailBase):
    """datos para crear una línea de pedido."""

    order_id: int
    product_id: int


class OrderDetailUpdate(BaseModel):
    """datos para actualizar una línea de pedido."""

    unit_price: float | None = None
    quantity: int | None = None
    discount: float | None = None


class OrderDetailRead(OrderDetailBase):
    """representación de una línea de pedido devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    order_id: int
    product_id: int
