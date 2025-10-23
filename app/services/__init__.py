from typing import Literal, Optional

from pydantic import ValidationError
import requests

from app.models.shared import ExternalApiData, ExternalApiResponse


class ExternalApiService:
    """Service for handling external API calls."""

    @staticmethod
    def fetch_post_data(post_id: int = 1) -> ExternalApiResponse:
        """
        Fetch post data from JSONPlaceholder API.

        Args:
            post_id: The ID of the post to fetch (default: 1)

        Returns:
            ExternalApiResponse containing the API call result
        """
        try:
            api_response = requests.get(
                f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout=5
            )
            api_data = api_response.json() if api_response.status_code == 200 else None
            external_api_status: Literal["success", "error"] = "success"
        except (requests.RequestException, ValueError):
            api_data = None
            external_api_status = "error"

        # Convert api_data to ExternalApiData if it exists
        external_api_data = None
        if api_data:
            try:
                # Use type-safe conversion with Pydantic
                external_api_data = ExternalApiData.model_validate(api_data)
            except ValidationError:
                external_api_status = "error"
                external_api_data = None

        return ExternalApiResponse(status=external_api_status, data=external_api_data)
