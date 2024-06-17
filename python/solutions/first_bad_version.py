class FirstBadVersion:
    """
    Problem:    278. First Bad Version
    Link:       https://leetcode.com/problems/first-bad-version/description/
    """

    def firstBadVersion(self, n: int) -> int:
        """
        Approach:   Employ a binary search to tackle this problem.
        TC:         O(logN)
        SC:         O(1)
        """
        l, r = 1, n + 1
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l


def isBadVersion(version: int) -> bool:
    """
    Mock the api provided by LeetCode
    """
    return version >= 4
