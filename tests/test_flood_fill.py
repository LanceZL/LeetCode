from solutions.flood_fill import FloodFill
from utils.test_case import Case


def test():
    """
    Tests for 733. Flood Fill
    """
    cases = [
        Case(
            params=[[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2],
            expect=[[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        Case(params=[[[0, 0, 0], [0, 0, 0]], 0, 0, 0], expect=[[0, 0, 0], [0, 0, 0]]),
        Case(
            params=[[[1, 1, 1], [1, 1, 1], [1, 1, 5]], 0, 0, 5],
            expect=[[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        ),
        Case(params=[[[0, 0, 0], [0, 0, 0]], 0, 0, 2], expect=[[2, 2, 2], [2, 2, 2]]),
    ]

    for c in cases:
        assert (
            FloodFill().floodFill(c.params[0], c.params[1], c.params[2], c.params[3])
            == c.expect
        )
