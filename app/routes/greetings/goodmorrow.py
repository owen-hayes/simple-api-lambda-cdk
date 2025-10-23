from fastapi import APIRouter

from app.models.greetings import GoodmorrowPersonDetails, GoodmorrowResponse


router = APIRouter()


@router.post(
    "/goodmorrow",
    response_model=GoodmorrowResponse,
    summary="Get good morrow message",
)
def get_goodmorrow_message(person: GoodmorrowPersonDetails) -> GoodmorrowResponse:
    """
    Get a nice good morrow message for a friend.
    """

    return GoodmorrowResponse(
        cool_message=f"Good morrow, {person.full_name}! Your favorite color is {person.favorite_color}.",
        email_to_display=person.email,
    )
