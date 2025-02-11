from python.solutions.valid_anagram import ValidAnagram
from python.utils.test_case import Case


def test():
    """
    Tests for 242. Valid Anagram.
    """
    cases = [
        Case(params=["anagram", "nagaram"], expect=True),
        Case(params=["rat", "car"], expect=False),
        Case(params=["rat", "ratt"], expect=False),
        Case(params=["bab", "ab"], expect=False),
    ]

    for testcase in cases:
        assert (
            ValidAnagram().isAnagram(testcase.params[0], testcase.params[1])
            == testcase.expect
        )
