from solutions.climbing_stairs import ClimbStairs
from utils.test_case import Case


def test_climb_stairs():
    """
    Tests for 70. Climbing Stairs.
    """
    cases = [
        Case(params=2, expect=2),
        Case(params=3, expect=3),
        Case(params=1, expect=1),
        Case(params=12, expect=233),
    ]

    for testcase in cases:
        assert ClimbStairs().climbStairs(testcase.params) == testcase.expect
