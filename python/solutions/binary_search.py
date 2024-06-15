from typing import List


class BinarySearch:
    """
    Problem:    704. Binary Search
    Link:       https://leetcode.com/problems/binary-search/description/
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        Approach:   Implements a binary search algorithm.
                    1.Use a left-closed, right-open interval [l, r).
                    2.Select the midpoint within [l, r) and compare it's value to the target value.
                    3.Adjust l or r based on the comparison result until the target is found or the interval [l, r) becomes invalid.
                    4.There is no need to check the final l, because according to our definition, if l equals r, then the l is definitely invalid.
        TC:         O(logN)
        SC:         O(1)
        """
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # Move l and r according to the nums[mid]
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return -1
