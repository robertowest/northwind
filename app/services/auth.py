"""servicio de autenticación: registro, validación de credenciales y emisión de tokens jwt."""

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.repositories.user import UserRepository


class AuthService:
    """concentra la lógica de negocio de autenticación."""

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def register(self, username: str, password: str) -> User:
        """damos de alta un usuario nuevo, guardando la contraseña ya hasheada."""
        return await self.repository.create(
            {'username': username, 'hashed_password': hash_password(password)}
        )

    async def authenticate(self, username: str, password: str) -> User | None:
        """validamos las credenciales y devolvemos el usuario si son correctas."""
        user = await self.repository.get_by_username(username)
        if (
            user is None
            or not user.is_active
            or not verify_password(password, user.hashed_password)
        ):
            return None
        return user

    def create_token_for(self, user: User) -> str:
        """generamos el jwt de acceso para un usuario ya autenticado."""
        return create_access_token(subject=user.username)
