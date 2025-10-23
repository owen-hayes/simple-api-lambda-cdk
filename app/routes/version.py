from fastapi import APIRouter
from app.models.version import VersionResponse
from app.version import get_build_info

router = APIRouter()


@router.get(
    "/version",
    response_model=VersionResponse,
    tags=["Other"],
    summary="Get version info",
)
def get_version_info() -> VersionResponse:
    """Get version and build information for the API."""

    build_info = get_build_info()

    return VersionResponse(
        version=build_info["version"],
        timestamp=build_info["timestamp"],
        source=build_info["source"],
        message=f"API Version {build_info['version']}",
    )
