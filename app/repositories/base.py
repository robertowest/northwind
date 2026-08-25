"""repositorio genérico con las operaciones crud básicas sobre un modelo sqlalchemy."""

from collections.abc import Sequence
from typing import Any

from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import Base


class BaseRepository[ModelType: Base]:
    """encapsula el acceso a datos de un modelo, con soporte para clave primaria simple o compuesta."""

    def __init__(self, session: AsyncSession, model: type[ModelType]) -> None:
        self.session = session
        self.model = model

    async def list(self, *, skip: int = 0, limit: int = 100) -> Sequence[ModelType]:
        """devolvemos un listado paginado de registros."""
        result = await self.session.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def get(self, **pk: Any) -> ModelType | None:
        """buscamos un registro por su clave primaria, respetando el orden real de las columnas."""
        pk_columns = [column.name for column in inspect(self.model).primary_key]
        if len(pk_columns) == 1:
            identity = pk[pk_columns[0]]
        else:
            identity = tuple(pk[column] for column in pk_columns)
        return await self.session.get(self.model, identity)

    async def create(self, data: dict[str, Any]) -> ModelType:
        """creamos un nuevo registro a partir de un diccionario de datos."""
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def update(self, instance: ModelType, data: dict[str, Any]) -> ModelType:
        """actualizamos los campos indicados de un registro ya existente."""
        for field, value in data.items():
            setattr(instance, field, value)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def delete(self, instance: ModelType) -> None:
        """eliminamos un registro existente."""
        await self.session.delete(instance)
        await self.session.commit()
