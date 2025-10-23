from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from . import docs, greetings, version

# Create main router
api_router = APIRouter()

# Root redirect to docs
@api_router.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """Redirect root endpoint to docs."""
    return RedirectResponse(url="/docs")

# Include all route modules
api_router.include_router(greetings.router)
api_router.include_router(docs.router)
api_router.include_router(version.router)
