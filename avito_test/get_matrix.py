"""Test case realizing."""
import aiohttp


def calculate_result(matrix: list[list[int]]) -> list[int]:
    """
    Process square matrix in a counterclockwork way.

    Args:
        matrix: square matrix

    Returns:
        New matrix
    """
    if matrix:
        return list(list(zip(*matrix))[0]) + calculate_result(
            list(zip(*matrix[::-1]))[1:],
        )
    return []


def _normalize_data(l_str: list[str]) -> list[int]:
    return [int(element.rstrip()) for element in l_str]


async def read_file(url: str) -> list[list[int]]:  # noqa: WPS210
    """
    Read matrix from URL and normalize it.

    Args:
        url: URL address

    Returns:
        Initial matrix
    """
    init_matrix = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.text()
            string = resp.split('\n')
            for line in string:
                temp = str(line).split('|')[1:-1]
                temp = _normalize_data(temp)
                if temp:
                    init_matrix.append(temp)
        await session.close()
    return init_matrix


async def get_matrix(url: str) -> list[int]:
    """
    Get matrix and process it in a counterclockwork way.

    Args:
        url: URL address

    Returns:
        One-dimensional list of processed matrix
    """
    matrix = await read_file(url)
    return calculate_result(matrix)
