from solutions.num_of_subarrays import NumOfSubarrays
from utils.test_case import Case


def test():
    cases = [
        Case(params=[[2, 2, 2, 2, 5, 5, 5, 8], 3, 4], expect=3),
        Case(params=[[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5], expect=6),
        Case(params=[[1, 1, 1, 1], 3, 0], expect=2),
    ]

    for c in cases:
        assert NumOfSubarrays().numOfSubarrays(*c.params) == c.expect
