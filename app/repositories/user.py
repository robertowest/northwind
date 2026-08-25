"""repositorio del modelo User, con la búsqueda adicional por username."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """añade a las operaciones genéricas la búsqueda por nombre de usuario, usada en el login."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User)

    async def get_by_username(self, username: str) -> User | None:
        """buscamos un usuario por su username."""
        result = await self.session.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
