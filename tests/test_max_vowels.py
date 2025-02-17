from solutions.maximum_vowels import MaxVowels
from utils.test_case import Case


def test():
    cases = [
        Case(params=["abciiidef", 3], expect=3),
        Case(params=["aeiou", 5], expect=5),
        Case(params=["aeki", 2], expect=2),
    ]

    for case in cases:
        assert MaxVowels().maxVowels(*case.params) == case.expect
