from solutions.maximum_average_subarray import FindMaxAverage
from utils.test_case import Case


def test():
    cases = [
        Case(params=[[1, 12, -5, -6, 50, 3], 4], expect=12.75000),
        Case(params=[[1], 1], expect=1.0000),
        Case(params=[[-1], 1], expect=-1.0000),
    ]

    for c in cases:
        assert FindMaxAverage().findMaxAverage(*c.params) == c.expect
