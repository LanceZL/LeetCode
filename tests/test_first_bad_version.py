from solutions.first_bad_version import FirstBadVersion
from utils.test_case import Case


def test():
    """Tests for 278. First Bad Version"""
    cases = [
        Case(params=5, expect=4),
        Case(params=872365278, expect=4),
    ]

    for testcase in cases:
        assert testcase.expect == FirstBadVersion().firstBadVersion(testcase.params)
