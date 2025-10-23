from pydantic import BaseModel, Field


class GoodbyeResponse(BaseModel):
    """
    Response given by the goodbye endpoint.
    """

    message: str = Field(..., description="The goodbye message", examples=["goodbye"])
    timestamp: str = Field(
        ...,
        description="The timestamp of the goodbye message",
        examples=["2024-01-15T10:30:45.123456"],
    )
