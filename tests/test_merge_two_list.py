from solutions.merge_two_list import MergeTwoLists
from utils.list_node import build_list
from utils.test_case import Case


def test():
    """Tests for merge two lists."""
    cases = [
        Case(params=[build_list(None), build_list(None)], expect=build_list(None)),
        Case(params=[build_list([]), build_list([])], expect=build_list([])),
        Case(params=[build_list([]), build_list([0])], expect=build_list([0])),
        Case(
            params=[build_list([1, 2, 3]), build_list([])], expect=build_list([1, 2, 3])
        ),
        Case(
            params=[build_list([2, 4, 6]), build_list([1, 3, 5])],
            expect=build_list([1, 2, 3, 4, 5, 6]),
        ),
        Case(
            params=[build_list([1, 4, 6]), build_list([1, 3, 5])],
            expect=build_list([1, 1, 3, 4, 5, 6]),
        ),
    ]

    for case in cases:
        assert (
            MergeTwoLists().mergeTwoLists(case.params[0], case.params[1]) == case.expect
        )
