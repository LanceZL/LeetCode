from solutions.k_radius_subarray_averages import KRadiusSubarrayAverages
from utils.test_case import Case


def test():
    cases = [
        Case(
            params=[[7, 4, 3, 9, 1, 8, 5, 2, 6], 3],
            expect=[-1, -1, -1, 5, 4, 4, -1, -1, -1],
        ),
        Case(params=[[100000], 0], expect=[100000]),
        Case(params=[[1], 10], expect=[-1]),
    ]

    for c in cases:
        assert KRadiusSubarrayAverages().getAverages(*c.params) == c.expect
