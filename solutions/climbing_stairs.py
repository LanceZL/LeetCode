class ClimbStairs:
    """
    Problem:    70. Climbing Stairs
    Link:       https://leetcode.com/problems/climbing-stairs/description/
    """

    # def climbStairs(self, n: int) -> int:
    #     """
    #         Approach:  For each step, the ways of it equals the way of the previos step and previous previous step.
    #                     F(n) = F(n-1) + F(n-2)
    #                     F(1) = 1
    #                     F(0) = 1
    #                     F(3) = F(2) + F(1) = F(0) + F(1) + F(1)
    #         TC:         O(2^N)
    #         SC:         O(LogN)

    #     """
    #     if n <= 1:
    #         return 1
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # def climbStairs(self, n: int) -> int:
    #     """
    #         Approach 2: Recursion with a memo.
    #         TC:         O(N)
    #         SC:         O(N)
    #     """
    #     memo = [None] * (n + 1)
    #     memo[0], memo[1] = 1, 1

    #     def cal(n) -> int:
    #         if memo[n] is not None:
    #             return memo[n]
    #         memo[n] = cal(n - 1) + cal(n - 2)
    #         return memo[n]

    #     return cal(n)

    def climbStairs(self, n: int) -> int:
        """
        Approach 3: DP
        """
        dp = [1] * (n + 1)

        i = 2
        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]
