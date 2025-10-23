import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.routes import api_router
from app.version import get_version

app = FastAPI(
    title="Simple API",
    description="A simple REST API.",
    version=get_version(),
    docs_url="/swagger",  # Disable default Swagger UI
    redoc_url=None,  # Disable default ReDoc
    openapi_tags=[
        {
            "name": "Greetings",
            "description": "Endpoints for greeting and farewell messages. These\
                endpoints provide personalized greetings and simple goodbye messages.",
        },
    ],

)

# Include all routes
app.include_router(api_router)

# Expose the Mangum adapter as the Lambda handler entrypoint (this is the magic thing that makes the API into an AWS Lambda function)
handler = Mangum(app)


def dev() -> None:
    """Development server with auto-reload."""
    uvicorn.run(
        "app.handler:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )


def start() -> None:
    """Production server."""
    uvicorn.run(
        "app.handler:app", host="0.0.0.0", port=8000, reload=False, log_level="info"
    )
