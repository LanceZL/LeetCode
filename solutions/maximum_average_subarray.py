from typing import List


class FindMaxAverage:
    """
    Problem: 643. Maximum Average Subarray I
    Link: https://leetcode.com/problems/maximum-average-subarray-i/description/
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Approach:
            - Use the sliding window technique to maintain a sum of `k` elements.
            - Slide the window across the array, updating the sum and tracking the maximum sum found.
            - Return the maximum sum divided by `k` to get the maximum average.
        TC: O(N)
        SC: O(1)
        """
        left = 0
        maximum, cur = float("-inf"), 0.0

        for right, num in enumerate(nums):
            # Append numbers into window
            cur += num

            if right - left + 1 < k:
                continue
            # update answer
            maximum = max(maximum, cur)

            # Move window
            cur -= nums[left]
            left += 1

        return maximum / k
