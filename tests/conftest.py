import pytest
from pathlib import Path


@pytest.fixture()
def root_path() -> Path:
    """Gets the tests root path."""
    return Path(__file__).parent


@pytest.fixture()
def data_path(root_path: Path) -> Path:
    """Gets the data path from tests path."""
    return root_path.joinpath("data")


@pytest.fixture()
def image_name():
    """Get this image name."""
    return "11743.jpg"


@pytest.fixture()
def image_buffer(data_path: Path, image_name: str) -> bytes:
    """Gets the image from path."""
    with open(data_path.joinpath(image_name), "rb") as file_in:
        buffer = file_in.read()

    return buffer


@pytest.fixture()
def object_name() -> str:
    """Returns object name"""
    return "aeroplane"
