from typing import List


class MaxProfit:
    """
    Problem     : 121. Best Time to Buy and Sell Stock
    Link        : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    """

    def maxProfit(self, nums: List[int]) -> int:
        """
        Solution                    : Use a DP table to track the local optimal solution.
                                      For each day, we have 2 state:
                                        1. Hold stock ->        dp[i][1]
                                        2. Don't hold stock->   dp[i][0]
        Base Case                   : dp[0][0] = 0, dp[0][1] = -nums[0]
        State transition equation   : dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
                                      dp[i][1] = max(-nums[i], dp[i - 1][1])
        TC                          : O(N)
        SC                          : O(N), from the dp table.
        Note                        : We can not carry over today's state of not holding a stock from yesterday's state,
                                        because we are only allowed to buy stock "ONCE".
        """
        n = len(nums)
        if n == 1:  # Corner Case.
            return 0

        dp = [[0] * 2 for j in range(n)]  # Init the dp table.
        dp[0][0], dp[0][1] = 0, -nums[0]  # Base case.

        # State transition
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
            dp[i][1] = max(0 - nums[i], dp[i - 1][1])

        # The maximum profit comes from not holding a stock.
        return dp[n - 1][0]
