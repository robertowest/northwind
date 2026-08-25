"""agregamos en un único router todos los endpoints de la versión 1 de la api."""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, customer_customer_demo, employee_territories, order_details
from app.api.v1.endpoints.crud_factory import build_crud_router
from app.models.category import Category
from app.models.customer import Customer
from app.models.customer_demographic import CustomerDemographic
from app.models.employee import Employee
from app.models.order import Order
from app.models.product import Product
from app.models.region import Region
from app.models.shipper import Shipper
from app.models.supplier import Supplier
from app.models.territory import Territory
from app.models.us_state import UsState
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.schemas.customer import CustomerCreate, CustomerRead, CustomerUpdate
from app.schemas.customer_demographic import (
    CustomerDemographicCreate,
    CustomerDemographicRead,
    CustomerDemographicUpdate,
)
from app.schemas.employee import EmployeeCreate, EmployeeRead, EmployeeUpdate
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.schemas.region import RegionCreate, RegionRead, RegionUpdate
from app.schemas.shipper import ShipperCreate, ShipperRead, ShipperUpdate
from app.schemas.supplier import SupplierCreate, SupplierRead, SupplierUpdate
from app.schemas.territory import TerritoryCreate, TerritoryRead, TerritoryUpdate
from app.schemas.us_state import UsStateCreate, UsStateRead, UsStateUpdate

api_router = APIRouter()

# routers con lógica propia (login/registro, o clave primaria compuesta)
api_router.include_router(auth.router)
api_router.include_router(order_details.router)
api_router.include_router(employee_territories.router)
api_router.include_router(customer_customer_demo.router)

# entidades con clave primaria simple: se registran a partir de la fábrica genérica
_simple_crud_entities = [
    {
        'model': Category,
        'pk_field': 'category_id',
        'pk_type': int,
        'read_schema': CategoryRead,
        'create_schema': CategoryCreate,
        'update_schema': CategoryUpdate,
        'prefix': '/categories',
        'tags': ['categories'],
    },
    {
        'model': Customer,
        'pk_field': 'customer_id',
        'pk_type': str,
        'read_schema': CustomerRead,
        'create_schema': CustomerCreate,
        'update_schema': CustomerUpdate,
        'prefix': '/customers',
        'tags': ['customers'],
    },
    {
        'model': CustomerDemographic,
        'pk_field': 'customer_type_id',
        'pk_type': str,
        'read_schema': CustomerDemographicRead,
        'create_schema': CustomerDemographicCreate,
        'update_schema': CustomerDemographicUpdate,
        'prefix': '/customer-demographics',
        'tags': ['customer_demographics'],
    },
    {
        'model': Employee,
        'pk_field': 'employee_id',
        'pk_type': int,
        'read_schema': EmployeeRead,
        'create_schema': EmployeeCreate,
        'update_schema': EmployeeUpdate,
        'prefix': '/employees',
        'tags': ['employees'],
    },
    {
        'model': Order,
        'pk_field': 'order_id',
        'pk_type': int,
        'read_schema': OrderRead,
        'create_schema': OrderCreate,
        'update_schema': OrderUpdate,
        'prefix': '/orders',
        'tags': ['orders'],
    },
    {
        'model': Product,
        'pk_field': 'product_id',
        'pk_type': int,
        'read_schema': ProductRead,
        'create_schema': ProductCreate,
        'update_schema': ProductUpdate,
        'prefix': '/products',
        'tags': ['products'],
    },
    {
        'model': Region,
        'pk_field': 'region_id',
        'pk_type': int,
        'read_schema': RegionRead,
        'create_schema': RegionCreate,
        'update_schema': RegionUpdate,
        'prefix': '/regions',
        'tags': ['region'],
    },
    {
        'model': Shipper,
        'pk_field': 'shipper_id',
        'pk_type': int,
        'read_schema': ShipperRead,
        'create_schema': ShipperCreate,
        'update_schema': ShipperUpdate,
        'prefix': '/shippers',
        'tags': ['shippers'],
    },
    {
        'model': Supplier,
        'pk_field': 'supplier_id',
        'pk_type': int,
        'read_schema': SupplierRead,
        'create_schema': SupplierCreate,
        'update_schema': SupplierUpdate,
        'prefix': '/suppliers',
        'tags': ['suppliers'],
    },
    {
        'model': Territory,
        'pk_field': 'territory_id',
        'pk_type': str,
        'read_schema': TerritoryRead,
        'create_schema': TerritoryCreate,
        'update_schema': TerritoryUpdate,
        'prefix': '/territories',
        'tags': ['territories'],
    },
    {
        'model': UsState,
        'pk_field': 'state_id',
        'pk_type': int,
        'read_schema': UsStateRead,
        'create_schema': UsStateCreate,
        'update_schema': UsStateUpdate,
        'prefix': '/us-states',
        'tags': ['us_states'],
    },
]

for entity in _simple_crud_entities:
    api_router.include_router(build_crud_router(**entity))
