"""endpoints crud de employee_territories (empleados <-> territorios, clave primaria compuesta)."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.employee_territory import EmployeeTerritory
from app.repositories.base import BaseRepository
from app.schemas.employee_territory import EmployeeTerritoryCreate, EmployeeTerritoryRead
from app.services.base import BaseService

router = APIRouter(prefix='/employee-territories', tags=['employee_territories'])


def get_service(db: AsyncSession = Depends(get_db)) -> BaseService[EmployeeTerritory]:
    """construimos el servicio genérico para el modelo EmployeeTerritory."""
    return BaseService(BaseRepository(db, EmployeeTerritory))


@router.get('', response_model=list[EmployeeTerritoryRead])
async def list_employee_territories(
    skip: int = 0, limit: int = 100, service: BaseService = Depends(get_service)
):
    """listamos las asociaciones empleado-territorio de forma paginada."""
    return await service.list(skip=skip, limit=limit)


@router.get('/{employee_id}/{territory_id}', response_model=EmployeeTerritoryRead)
async def get_employee_territory(
    employee_id: int, territory_id: str, service: BaseService = Depends(get_service)
):
    """obtenemos una asociación empleado-territorio por su clave compuesta."""
    instance = await service.get(employee_id=employee_id, territory_id=territory_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'asociación no encontrada')
    return instance


@router.post('', response_model=EmployeeTerritoryRead, status_code=status.HTTP_201_CREATED)
async def create_employee_territory(
    payload: EmployeeTerritoryCreate,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """asociamos un empleado a un territorio (requiere autenticación)."""
    existing = await service.get(employee_id=payload.employee_id, territory_id=payload.territory_id)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, 'la asociación ya existe')
    return await service.create(payload.model_dump())


@router.delete('/{employee_id}/{territory_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee_territory(
    employee_id: int,
    territory_id: str,
    service: BaseService = Depends(get_service),
    _user=Depends(get_current_user),
):
    """eliminamos una asociación empleado-territorio (requiere autenticación)."""
    instance = await service.get(employee_id=employee_id, territory_id=territory_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'asociación no encontrada')
    await service.delete(instance)
