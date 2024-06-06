from python.utils.test_case import Case
from python.utils.list_node import LinkedList


class TestList:
    """Unit tests for List and ListNode"""
    def test_build_a_list(self):
        """
            Build a list then compare the value of this list.
        """
        cases = [
            Case(
                params=[],
                expect=None
            ),
            Case(
                params=None,
                expect=None
            ),
            Case(
                params=[1],
                expect=[1]
            ),
            Case(
                params=[1, 2, 3],
                expect=[1, 2, 3]
            )
        ]

        for case in cases:
            assert LinkedList.value_of(LinkedList.build_list(case.params)) == case.expect

    def test_format_of_list(self):
        """Test the format of a list string."""
        cases = [
            Case(
                params=[],
                expect=""
            ),
            Case(
                params=[1],
                expect="1"
            ),
            Case(
                params=[1, 2, 3],
                expect="1 -> 2 -> 3"
            )
        ]

        for case in cases:
            assert LinkedList.print_list(LinkedList.build_list(case.params)) == case.expect

    def test_compare_list(self):
        """Test if two lists are equal"""
        cases = [
            Case(
                params=[
                    LinkedList.build_list([]),
                    LinkedList.build_list([])
                ],
                expect=True
            ),
            Case(
                params=[
                    LinkedList.build_list(None),
                    LinkedList.build_list([])
                ],
                expect=True
            ),
            Case(
                params=[
                    LinkedList.build_list([1]),
                    LinkedList.build_list([])
                ],
                expect=False
            ),
            Case(
                params=[
                    LinkedList.build_list([1]),
                    LinkedList.build_list([1])
                ],
                expect=True
            ),
            Case(
                params=[
                    LinkedList.build_list([1]),
                    LinkedList.build_list([1,2,3,4])
                ],
                expect=False
            ),
            Case(
                params=[
                    LinkedList.build_list([1,2,3,4]),
                    LinkedList.build_list([1,2,3,4])
                ],
                expect=True
            ),
            Case(
                params=[
                    LinkedList.build_list([1,2,3,4]),
                    LinkedList.build_list([4,3,2,1])
                ],
                expect=False
            ),
        ]

        for case in cases:
            assert LinkedList.compare(case.params[0], case.params[1]) == case.expect
