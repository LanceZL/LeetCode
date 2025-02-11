from python.solutions.binary_search import BinarySearch
from python.utils.test_case import Case


def test():
    """
    Tests for 704. Binary Search.
    """
    cases = [
        Case(params=[[-1, 0, 3, 5, 9, 12], 9], expect=4),
        Case(params=[[-1, 0, 3, 5, 9, 12], 2], expect=-1),
        Case(params=[[-1, 0, 3, 5, 9, 12], -1], expect=0),
        Case(params=[[-1, 0, 3, 5, 9, 12], 12], expect=5),
        Case(params=[[-1, 0, 3, 5, 9, 12], 16], expect=-1),
        Case(params=[[-1, 0, 3, 5, 9, 12], -50], expect=-1),
    ]

    for testcase in cases:
        assert (
            BinarySearch().search(testcase.params[0], testcase.params[1])
            == testcase.expect
        )
