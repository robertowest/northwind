"""esquemas de la entidad category."""

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    """campos comunes de una categoría."""

    category_name: str
    description: str | None = None


class CategoryCreate(CategoryBase):
    """datos para crear una categoría. la bd no autogenera el id, hay que indicarlo."""

    category_id: int


class CategoryUpdate(BaseModel):
    """datos para actualizar una categoría, todos opcionales."""

    category_name: str | None = None
    description: str | None = None


class CategoryRead(CategoryBase):
    """representación de una categoría devuelta por la api."""

    model_config = ConfigDict(from_attributes=True)

    category_id: int
