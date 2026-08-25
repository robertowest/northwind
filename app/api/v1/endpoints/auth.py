"""endpoints de autenticación: registro de usuarios y login (emisión de jwt)."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.user import UserRepository
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserRead
from app.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['auth'])


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    """construimos el servicio de autenticación con su repositorio."""
    return AuthService(UserRepository(db))


@router.post('/register', response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(payload: UserCreate, service: AuthService = Depends(get_auth_service)):
    """damos de alta un usuario nuevo."""
    existing = await service.repository.get_by_username(payload.username)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, 'el username ya está en uso')
    return await service.register(payload.username, payload.password)


@router.post('/login', response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    """validamos las credenciales y devolvemos el jwt de acceso."""
    user = await service.authenticate(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            'credenciales incorrectas',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return Token(access_token=service.create_token_for(user))
