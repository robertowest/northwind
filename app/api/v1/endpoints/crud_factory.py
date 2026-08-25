"""fábrica de routers crud genéricos para entidades con clave primaria simple.

evitamos repetir el mismo router para cada una de las tablas de northwind: basta con
indicar el modelo, sus esquemas y el nombre/tipo de su clave primaria.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.base import Base
from app.repositories.base import BaseRepository
from app.services.base import BaseService


def build_crud_router(
    *,
    model: type[Base],
    pk_field: str,
    pk_type: type,
    read_schema: type[BaseModel],
    create_schema: type[BaseModel],
    update_schema: type[BaseModel],
    prefix: str,
    tags: list[str],
) -> APIRouter:
    """construimos un router con el crud estándar (list/get/create/update/delete) para un modelo."""
    router = APIRouter(prefix=prefix, tags=tags)

    def get_service(db: AsyncSession = Depends(get_db)) -> BaseService:
        return BaseService(BaseRepository(db, model))

    @router.get('', response_model=list[read_schema])
    async def list_items(
        skip: int = 0,
        limit: int = 100,
        service: BaseService = Depends(get_service),
    ):
        """listamos los registros de forma paginada."""
        return await service.list(skip=skip, limit=limit)

    @router.get('/{item_id}', response_model=read_schema)
    async def get_item(item_id: pk_type, service: BaseService = Depends(get_service)):
        """obtenemos un registro por su clave primaria."""
        instance = await service.get(**{pk_field: item_id})
        if instance is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'registro no encontrado')
        return instance

    @router.post('', response_model=read_schema, status_code=status.HTTP_201_CREATED)
    async def create_item(
        payload: create_schema,
        service: BaseService = Depends(get_service),
        _user=Depends(get_current_user),
    ):
        """creamos un registro nuevo (requiere autenticación)."""
        existing = await service.get(**{pk_field: getattr(payload, pk_field)})
        if existing is not None:
            raise HTTPException(status.HTTP_409_CONFLICT, 'el registro ya existe')
        return await service.create(payload.model_dump())

    @router.put('/{item_id}', response_model=read_schema)
    async def update_item(
        item_id: pk_type,
        payload: update_schema,
        service: BaseService = Depends(get_service),
        _user=Depends(get_current_user),
    ):
        """actualizamos parcialmente un registro existente (requiere autenticación)."""
        instance = await service.get(**{pk_field: item_id})
        if instance is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'registro no encontrado')
        return await service.update(instance, payload.model_dump(exclude_unset=True))

    @router.delete('/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
    async def delete_item(
        item_id: pk_type,
        service: BaseService = Depends(get_service),
        _user=Depends(get_current_user),
    ):
        """eliminamos un registro existente (requiere autenticación)."""
        instance = await service.get(**{pk_field: item_id})
        if instance is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'registro no encontrado')
        await service.delete(instance)

    return router
