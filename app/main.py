"""punto de entrada de la aplicación fastapi."""

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.project_name)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get('/health', tags=['health'])
async def health() -> dict[str, str]:
    """comprobamos que el servicio está levantado, sin tocar la base de datos."""
    return {'status': 'ok'}
