from python.utils.list_node import build_list
from python.utils.test_case import Case


class TestList:
    """Unit tests for List and ListNode"""

    def test_build_a_list(self):
        """
        Build a list then compare the value of this list.
        """
        cases = [
            Case(params=[], expect=None),
            Case(params=None, expect=None),
            Case(params=[1], expect=[1]),
            Case(params=[1, 2, 3], expect=[1, 2, 3]),
        ]

        for case in cases:
            assert build_list(case.params) == build_list(case.expect)

    def test_list_string(self):
        """Test the format of a list string."""
        cases = [
            Case(params=[], expect="None"),
            Case(params=[1], expect="1"),
            Case(params=[0, 0], expect="0 -> 0"),
            Case(params=[1, 2, 3], expect="1 -> 2 -> 3"),
        ]

        for case in cases:
            assert str(build_list(case.params)) == case.expect

    def test_list_equals(self):
        """Test if two lists are equal"""
        cases = [
            Case(params=[build_list([]), build_list([])], expect=True),
            Case(params=[build_list(None), build_list([])], expect=True),
            Case(params=[build_list([0]), build_list([])], expect=False),
            Case(params=[build_list([0]), build_list([0])], expect=True),
            Case(params=[build_list([1]), build_list([1])], expect=True),
            Case(params=[build_list([1]), build_list([1, 2, 3, 4])], expect=False),
            Case(
                params=[build_list([1, 2, 3, 4]), build_list([1, 2, 3, 4])], expect=True
            ),
            Case(
                params=[build_list([1, 2, 3, 4]), build_list([4, 3, 2, 1])],
                expect=False,
            ),
        ]

        for case in cases:
            assert (case.params[0] == case.params[1]) == case.expect
