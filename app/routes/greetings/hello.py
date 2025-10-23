import datetime

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.models.greetings import HelloResponse, HelloTeapotResponse
from app.services import ExternalApiService

router = APIRouter()


GLOBAL_TEAPOT = False


@router.get(
    "/hello",
    summary="Get personalized hello message",
    response_model=None,
    responses={
        200: {
            "model": HelloResponse,
        },
        418: {
            "model": HelloTeapotResponse,
        },
    },
)
def get_hello_message(
    name: str = Query(
        None,
        description="The name to include in the greeting message",
        examples=["John"],
        min_length=1,
        max_length=50,
    ),
    # TODO: Add these back and do something with filters
    # filters: FilterParams = Query(
    #     default=FilterParams(),
    #     description="Filter parameters for data retrieval",
    # ),
) -> HelloResponse | JSONResponse:
    """
    Get a simple "hello" message.

    Personalization optional.

    Also fetches data from an external API to demonstrate API integration.
    """

    if GLOBAL_TEAPOT:
        return JSONResponse(content=HelloTeapotResponse().model_dump(), status_code=418)

    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Use the external API service
    external_api_response = ExternalApiService.fetch_post_data()

    message = f"Hello {name} from FastAPI" if name else "Hello from FastAPI"

    return HelloResponse(
        message=message,
        timestamp=timestamp,
        external_api_call=external_api_response,
    )
