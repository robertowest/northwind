"""test del endpoint de health-check."""

from httpx import ASGITransport, AsyncClient

from app.main import app


async def test_health() -> None:
    """comprobamos que /health responde 200 con el status esperado."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as client:
        response = await client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
