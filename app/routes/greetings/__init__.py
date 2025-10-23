from fastapi import APIRouter

from app.routes.greetings import goodmorrow, hello, goodbye

# Create greetings router
router = APIRouter(tags=["Greetings"])

# Include greeting route modules
router.include_router(hello.router)
router.include_router(goodbye.router)
router.include_router(goodmorrow.router)
