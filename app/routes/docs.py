from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference

from app.routes.version import router

router = APIRouter()
app = FastAPI()


@router.get("/docs", include_in_schema=False)
async def scalar_html() -> HTMLResponse:
    """
    Serve Scalar API documentation.

    Scalar is a tool that generates nice-looking API documentation from OpenAPI spec. It
    is an alternative to Swagger UI (which is not visually appealing to me).

    See https://guides.scalar.com/scalar/scalar-api-references/integrations/fastapi for
    more information.
    """

    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        # Avoid CORS issues (optional)
        scalar_proxy_url="https://proxy.scalar.com",
        title="Simple API",
    )
