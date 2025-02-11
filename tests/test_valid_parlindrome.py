from solutions.valid_palindrome import ValidParlindrome
from utils.test_case import Case


def test():
    """Tests for 125. Valid Palindrome"""
    cases = [
        Case(params="A man, a plan, a canal: Panama", expect=True),
        Case(params="race a car", expect=False),
        Case(params=" ", expect=True),
        Case(params="###########", expect=True),
        Case(params="####!!&&&", expect=True),
    ]

    for testcase in cases:
        assert ValidParlindrome().isPalindrome(testcase.params) == testcase.expect
