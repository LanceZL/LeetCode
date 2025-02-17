from solutions.ransom_note import RansomNote
from utils.test_case import Case


def test():
    testcases = [
        Case(params=["a", "b"], expect=False),
        Case(params=["aa", "ab"], expect=False),
        Case(params=["acajghs", "bajsfgh"], expect=False),
        Case(params=["aa", "aab"], expect=True),
        Case(params=["abcd", "dbcsa"], expect=True),
    ]

    for testcase in testcases:
        assert RansomNote().canConstruct(testcase.params[0], testcase.params[1]) == testcase.expect
