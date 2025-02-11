from solutions.sell_stock_I import MaxProfit
from utils.test_case import Case


def test():
    """
    Tests for 121:Best Time to Buy and Sell Stock
    """
    cases = [
        Case(params=[1, 5], expect=4),
        Case(params=[5, 1], expect=0),
        Case(params=[7, 1, 5, 3, 6, 4], expect=5),
        Case(params=[7, 6, 4, 3, 1], expect=0),
        Case(params=[1], expect=0),
    ]

    for case in cases:
        assert MaxProfit().maxProfit(case.params) == case.expect
