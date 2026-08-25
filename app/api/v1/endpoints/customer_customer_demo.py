"""endpoints crud de customer_customer_demo (clientes <-> perfiles demográficos, pk compuesta)."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.customer_customer_demo import CustomerCustomerDemo
from app.repositories.base import BaseRepository
from app.schemas.customer_customer_demo import (
    CustomerCustomerDemoCreate,
    CustomerCustomerDemoRead,
)
from app.services.base import BaseService

router = APIRouter(prefix='/customer-customer-demo', tags=['customer_customer_demo'])


def get_service(db: AsyncSession = Depends(get_db)) -> BaseService[CustomerCustomerDemo]:
    """construimos el servicio genérico para el modelo CustomerCustomerDemo."""
    return BaseService(BaseRepository(db, CustomerCustomerDemo))


@router.get('', response_model=list[CustomerCustomerDemoRead])
async def list_customer_customer_demo(
    skip: int = 0, limit: int = 100, service: BaseService = Depends(get_service)
):
    """listamos las asociaciones cliente-perfil demográfico de forma paginada."""
    return await service.list(skip=skip, limit=limit)


@router.get('/{customer_id}/{customer_type_id}', response_model=CustomerCustomerDemoRead)
async def get_customer_customer_demo(
    customer_id: str, customer_type_id: str, service: BaseService = Depends(get_service)
):
    """obtenemos una asociación cliente-perfil demográfico por su clave compuesta."""
    instance = await service.get(customer_id=customer_id, customer_type_id=customer_type_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'asociación no encontrada')
    return instance


@router.post('', response_model=CustomerCustomerDemoRead, status_code=status.HTTP_201_CREATED)
async def create_customer_customer_demo(
    payload: CustomerCustomerDemoCreate,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """asociamos un cliente a un perfil demográfico (requiere autenticación)."""
    existing = await service.get(
        customer_id=payload.customer_id, customer_type_id=payload.customer_type_id
    )
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, 'la asociación ya existe')
    return await service.create(payload.model_dump())


@router.delete('/{customer_id}/{customer_type_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_customer_demo(
    customer_id: str,
    customer_type_id: str,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """eliminamos una asociación cliente-perfil demográfico (requiere autenticación)."""
    instance = await service.get(customer_id=customer_id, customer_type_id=customer_type_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'asociación no encontrada')
    await service.delete(instance)
