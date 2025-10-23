from typing import Literal, Optional
from pydantic import BaseModel, EmailStr, Field

from app.models.shared import ExternalApiResponse


class HelloResponse(BaseModel):
    """Response model for the hello endpoint."""

    message: str = Field(
        default=...,
        description="Greeting message",
        examples=["Hello John from FastAPI"],
    )
    timestamp: str = Field(
        default=...,
        description="ISO timestamp of the response",
        examples=["2024-01-15T10:30:45.123456"],
    )
    external_api_call: ExternalApiResponse = Field(
        default=..., description="External API call result"
    )
    # requests_version: str = Field(
    #     default=..., description="Version of the requests library", examples=["2.31.0"]
    # )


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


ColorsOfRainbow = Literal[
    "red", "orange", "yellow", "green", "blue", "indigo", "violet"
]


class GoodmorrowPersonDetails(BaseModel):
    """Details about the person to say good morrow to."""

    full_name: str = Field(
        default=...,
        description="The full name of the person.",
        examples=["Susie Q", "Johnny B"],
    )

    email: Optional[EmailStr] = Field(
        default=None,
        description="The person's email.",
        examples=["susie.q@gmail.com"],
    )

    favorite_color: ColorsOfRainbow = Field(
        description="The person's favorite color.", examples=["indigo"]
    )


class GoodmorrowResponse(BaseModel):
    """
    Response given by the good morrow endpoint.
    """

    cool_message: str = Field(
        ...,
        description="The good morrow message",
        examples=["Good morrow, Susie Q! Your favorite color is purple."],
    )

    email_to_display: Optional[EmailStr] = Field(
        default=None,
        description="The email of the person to display on the frontend.",
        examples=["susie.q@gmail.com"],
    )


class HelloTeapotResponse(BaseModel):
    """Response for when the client is a teapot."""

    teapot_text: str = Field(
        description="Some teapot-related text", examples=["🫖🫖🫖"], default="🫖🫖🫖"
    )
