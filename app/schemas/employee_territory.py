"""esquemas de la entidad puente employee_territory."""

from pydantic import BaseModel, ConfigDict


class EmployeeTerritoryCreate(BaseModel):
    """datos para asociar un empleado a un territorio."""

    employee_id: int
    territory_id: str


class EmployeeTerritoryRead(BaseModel):
    """representación de la asociación empleado <-> territorio."""

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    territory_id: str
