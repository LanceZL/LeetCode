from solutions.Minimum_Recolors_to_Get_K_Consecutive_Black_Blocks import MinimumRecolors
from utils.test_case import Case


def test():
    cases = [
        Case(params=["WBBWWBBWBW", 7], expect=3),
        Case(params=["WBWBBBW", 2], expect=0),
        Case(params=["WWWWWWW", 7], expect=7),
    ]

    for case in cases:
        assert MinimumRecolors().minimumRecolors(*case.params) == case.expect
