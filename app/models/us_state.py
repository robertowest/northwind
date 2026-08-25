"""modelo de la tabla us_states (catálogo auxiliar, sin relaciones fk en el esquema)."""

from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class UsState(Base):
    """catálogo de estados de ee. uu."""

    __tablename__ = 'us_states'

    state_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    state_name: Mapped[str | None] = mapped_column(String(100))
    state_abbr: Mapped[str | None] = mapped_column(String(2))
    state_region: Mapped[str | None] = mapped_column(String(50))
