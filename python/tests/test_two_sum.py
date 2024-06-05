from solutions.two_sum import TwoSum
from .base_test_case import Case

def test():
    """Test Two Sum"""
    cases = [
        Case(
            params = [[0, 1], 1],
            expect = [0, 1]
        ),
        ]

    for case in cases:
        assert TwoSum().twoSum(case.params[0], case.params[1]) == case.expect
