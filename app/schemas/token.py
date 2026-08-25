"""esquemas relacionados con la autenticación jwt."""

from pydantic import BaseModel


class Token(BaseModel):
    """respuesta devuelta al iniciar sesión correctamente."""

    access_token: str
    token_type: str = 'bearer'
