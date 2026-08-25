"""endpoints crud de order_details (líneas de pedido, clave primaria compuesta)."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.order_detail import OrderDetail
from app.repositories.base import BaseRepository
from app.schemas.order_detail import OrderDetailCreate, OrderDetailRead, OrderDetailUpdate
from app.services.base import BaseService

router = APIRouter(prefix='/order-details', tags=['order_details'])


def get_service(db: AsyncSession = Depends(get_db)) -> BaseService[OrderDetail]:
    """construimos el servicio genérico para el modelo OrderDetail."""
    return BaseService(BaseRepository(db, OrderDetail))


@router.get('', response_model=list[OrderDetailRead])
async def list_order_details(
    skip: int = 0, limit: int = 100, service: BaseService = Depends(get_service)
):
    """listamos las líneas de pedido de forma paginada."""
    return await service.list(skip=skip, limit=limit)


@router.get('/{order_id}/{product_id}', response_model=OrderDetailRead)
async def get_order_detail(
    order_id: int, product_id: int, service: BaseService = Depends(get_service)
):
    """obtenemos una línea de pedido por su clave compuesta."""
    instance = await service.get(order_id=order_id, product_id=product_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'línea de pedido no encontrada')
    return instance


@router.post('', response_model=OrderDetailRead, status_code=status.HTTP_201_CREATED)
async def create_order_detail(
    payload: OrderDetailCreate,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """creamos una línea de pedido nueva (requiere autenticación)."""
    existing = await service.get(order_id=payload.order_id, product_id=payload.product_id)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, 'la línea de pedido ya existe')
    return await service.create(payload.model_dump())


@router.put('/{order_id}/{product_id}', response_model=OrderDetailRead)
async def update_order_detail(
    order_id: int,
    product_id: int,
    payload: OrderDetailUpdate,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """actualizamos una línea de pedido existente (requiere autenticación)."""
    instance = await service.get(order_id=order_id, product_id=product_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'línea de pedido no encontrada')
    return await service.update(instance, payload.model_dump(exclude_unset=True))


@router.delete('/{order_id}/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_detail(
    order_id: int,
    product_id: int,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """eliminamos una línea de pedido existente (requiere autenticación)."""
    instance = await service.get(order_id=order_id, product_id=product_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'línea de pedido no encontrada')
    await service.delete(instance)
