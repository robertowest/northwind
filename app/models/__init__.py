"""exponemos todos los modelos para que Base.metadata los conozca (usado por alembic)."""

from app.models.base import Base
from app.models.category import Category
from app.models.customer import Customer
from app.models.customer_customer_demo import CustomerCustomerDemo
from app.models.customer_demographic import CustomerDemographic
from app.models.employee import Employee
from app.models.employee_territory import EmployeeTerritory
from app.models.order import Order
from app.models.order_detail import OrderDetail
from app.models.product import Product
from app.models.region import Region
from app.models.shipper import Shipper
from app.models.supplier import Supplier
from app.models.territory import Territory
from app.models.us_state import UsState
from app.models.user import User

__all__ = [
    'Base',
    'Category',
    'Customer',
    'CustomerCustomerDemo',
    'CustomerDemographic',
    'Employee',
    'EmployeeTerritory',
    'Order',
    'OrderDetail',
    'Product',
    'Region',
    'Shipper',
    'Supplier',
    'Territory',
    'UsState',
    'User',
]
