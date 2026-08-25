"""dependencias comunes de la capa api: sesión de bd y resolución del usuario autenticado."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User
from app.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.api_v1_prefix}/auth/login')


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    """resolvemos el usuario autenticado a partir del token jwt de la petición."""
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='no se han podido validar las credenciales',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    username = decode_access_token(token)
    if username is None:
        raise credentials_error
    user = await UserRepository(db).get_by_username(username)
    if user is None or not user.is_active:
        raise credentials_error
    return user
