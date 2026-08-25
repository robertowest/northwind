"""esquemas de la entidad product."""

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    """campos comunes de un producto."""

    product_name: str
    supplier_id: int | None = None
    category_id: int | None = None
    quantity_per_unit: str | None = None
    unit_price: float | None = None
    units_in_stock: int | None = None
    units_on_order: int | None = None
    reorder_level: int | None = None
    discontinued: int = 0


class ProductCreate(ProductBase):
    """datos para crear un producto."""

    product_id: int


class ProductUpdate(BaseModel):
    """datos para actualizar un producto, todos opcionales."""

    product_name: str | None = None
    supplier_id: int | None = None
    category_id: int | None = None
    quantity_per_unit: str | None = None
    unit_price: float | None = None
    units_in_stock: int | None = None
    units_on_order: int | None = None
    reorder_level: int | None = None
    discontinued: int | None = None


class ProductRead(ProductBase):
    """representación de un producto devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    product_id: int
