from typing import Literal

from pydantic import BaseModel, Field


class VersionResponse(BaseModel):
    """
    Response from the version endpoint.
    """

    version: str = Field(
        description="The version of the API", examples=["2025.10.17.1606"]
    )

    timestamp: str = Field(
        description="When this response was generated",
        examples=["2025-10-17T21:14:42.301Z"],
    )

    source: Literal["deployment", "local"] = Field(
        default="local",
        description="Whether this is a deployment build or local development",
        examples=["local", "deployment"],
    )

    message: str = Field(
        description="Message about the API version",
        examples=["API Version 2025.10.17.1606"],
    )
