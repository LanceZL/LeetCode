from solutions.valid_parentheses import ValidParentheses
from utils.test_case import Case


def test():
    """Test Valid Parentheses"""
    cases = [
        Case(
            params="((())",
            expect=False,
        ),
        Case(
            params="",
            expect=False,
        ),
        Case(
            params="((()))",
            expect=True,
        ),
        Case(
            params=")))((",
            expect=False,
        ),
        Case(
            params="({[]})",
            expect=True,
        ),
        Case(
            params="((()]}",
            expect=False,
        ),
        Case(
            params="(]",
            expect=False,
        ),
        Case(
            params="()",
            expect=True,
        ),
        Case(
            params="[]",
            expect=True,
        ),
        Case(
            params="()[]",
            expect=True,
        ),
        Case(
            params="{}",
            expect=True,
        ),
        Case(
            params="()[]{}",
            expect=True,
        ),
    ]

    for case in cases:
        assert ValidParentheses().isValid(case.params) == case.expect
