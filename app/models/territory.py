"""modelo de la tabla territories."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.employee_territory import EmployeeTerritory
    from app.models.region import Region


class Territory(Base):
    """territorio de ventas, agrupado en una región."""

    __tablename__ = 'territories'

    territory_id: Mapped[str] = mapped_column(String(20), primary_key=True)
    territory_description: Mapped[str] = mapped_column(String(60))
    region_id: Mapped[int] = mapped_column(SmallInteger, ForeignKey('region.region_id'))

    region: Mapped['Region'] = relationship(back_populates='territories')
    employees: Mapped[list['EmployeeTerritory']] = relationship(back_populates='territory')
