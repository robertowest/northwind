"""servicio genérico: punto único donde añadir reglas de negocio sobre un modelo."""

from collections.abc import Sequence
from typing import Any

from app.models.base import Base
from app.repositories.base import BaseRepository


class BaseService[ModelType: Base]:
    """orquesta las operaciones crud delegando el acceso a datos en el repositorio.

    las vistas (routers) nunca acceden al repositorio directamente: siempre pasan por aquí,
    que es donde deben añadirse las validaciones o reglas de negocio de cada entidad.
    """

    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        self.repository = repository

    async def list(self, *, skip: int = 0, limit: int = 100) -> Sequence[ModelType]:
        """listamos los registros de forma paginada."""
        return await self.repository.list(skip=skip, limit=limit)

    async def get(self, **pk: Any) -> ModelType | None:
        """obtenemos un registro por su clave primaria."""
        return await self.repository.get(**pk)

    async def create(self, data: dict[str, Any]) -> ModelType:
        """creamos un registro nuevo."""
        return await self.repository.create(data)

    async def update(self, instance: ModelType, data: dict[str, Any]) -> ModelType:
        """actualizamos un registro existente."""
        return await self.repository.update(instance, data)

    async def delete(self, instance: ModelType) -> None:
        """eliminamos un registro existente."""
        await self.repository.delete(instance)
