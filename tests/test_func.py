"""Test function for processing square matrix in a counterclockwork way."""

import asyncio

from avito_test.get_matrix import get_matrix

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'  # noqa: E501
TRAVERSAL = [  # noqa: WPS407, WPS317
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    """Test function."""
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL  # noqa: S101
