from typing import Literal, Optional

from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    """
    Filter parameters for querying data.

    This model defines the available filtering options for data retrieval,
    including pagination, sorting, and tag filtering capabilities.
    """

    model_config = {"extra": "forbid"}

    limit: int = Field(
        default=100,
        gt=0,
        le=100,
        description="Maximum number of items to return",
        examples=[50],
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="Number of items to skip (for pagination)",
        examples=[0],
    )
    order_by: Literal["created_at", "updated_at"] = Field(
        default="created_at",
        description="Field to sort results by",
        examples=["created_at"],
    )
    tags: list[str] = Field(
        default=[],
        description="List of tags to filter by",
        examples=[["python", "api"]],
    )


class ExternalApiData(BaseModel):
    """Data structure for external API response."""

    userId: int = Field(
        default=..., description="User ID from external API", examples=[1]
    )
    id: int = Field(default=..., description="Post ID from external API", examples=[1])
    title: str = Field(
        default=...,
        description="Post title from external API",
        examples=[
            "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        ],
    )
    body: str = Field(
        default=...,
        description="Post body content from external API",
        examples=[
            """quia et suscipit\nsuscipit recusandae consequuntur expedita et cum
            reprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem
            eveniet architecto"""
        ],
    )


class ExternalApiResponse(BaseModel):
    """External API response structure."""

    status: Literal["success", "error"] = Field(
        default=..., description="Status of the external API call", examples=["success"]
    )
    data: Optional[ExternalApiData] = Field(
        default=None, description="Data from external API, null if error"
    )
