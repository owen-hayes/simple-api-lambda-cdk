"""
Version management for the application.

This module provides dynamic version generation based on date/time,
with support for environment variable override for deployment builds.
"""

import datetime
import os
from typing import Literal, TypedDict


class BuildInfo(TypedDict):
    """Build information structure."""
    version: str
    timestamp: str
    source: Literal["deployment", "local"]


def get_version() -> str:
    """
    Get the application version.

    Priority:
    1. VERSION environment variable (set during deployment)
    2. Dynamic generation based on current date/time (for local development)

    Returns:
        str: Version string in format YYYY.MM.DD.HHMM
    """
    # Check if version is set via environment variable (deployment)
    env_version = os.getenv("VERSION")
    if env_version:
        return env_version

    # Generate version based on current date/time (local development)
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime("%Y.%m.%d.%H%M")


def get_build_info() -> BuildInfo:
    """
    Get build information including version and timestamp.

    Returns:
        BuildInfo: Build information with version, timestamp, and source
    """
    version = get_version()
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Determine if this is a deployment build or local development
    source: Literal["deployment", "local"] = (
        "deployment" if os.getenv("VERSION") else "local"
    )

    return {
        "version": version,
        "timestamp": timestamp,
        "source": source,
    }


# Export the version for easy import
__version__ = get_version()
