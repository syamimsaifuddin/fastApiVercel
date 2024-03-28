from fastapi import APIRouter

swagger_router = APIRouter()

@swagger_router.get("/docs")
async def get_documentation():
    """Serve Swagger UI."""
    return swagger_router.openapi_html()

# Serve ReDoc
@swagger_router.get("/redoc")
async def get_redoc():
    """Serve ReDoc."""
    return swagger_router.openapi_redoc()