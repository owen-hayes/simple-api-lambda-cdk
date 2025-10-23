import datetime

from fastapi import APIRouter

from app.models.greetings import GoodbyeResponse

router = APIRouter()


@router.get(
    "/goodbye",
    response_model=GoodbyeResponse,
    summary="Get goodbye message",
)
def get_goodbye_message() -> GoodbyeResponse:
    """
    Get a basic goodbye response.
    """
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return GoodbyeResponse(message="goodbye", timestamp=timestamp)
