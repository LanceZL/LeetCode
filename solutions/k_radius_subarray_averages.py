from typing import List


class KRadiusSubarrayAverages:
    """
    2090. K Radius Subarray Averages
    https://leetcode.com/problems/k-radius-subarray-averages/description/
    """

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
        Approach:
            - Utilize a fixed sliding window to maintain the sum of elements.
            - Convert the given radius `k` into a window size: `size = 2 * k + 1`.
            - The center of the window is positioned at `right - k` while iterating.
        TC: O(N) as it only iterates through the array in constant times
        SC: O(1) as it only use a constant number of variables.
        """
        # Egde case
        if k == 0:
            return nums

        res = [-1 for i in nums]
        if k > len(nums):
            return res

        size = 2 * k + 1
        left = cur_sum = 0
        for right, num in enumerate(nums):
            cur_sum += num

            if right - left + 1 < size:
                continue

            # update res
            res[right - k] = cur_sum // size

            cur_sum -= nums[left]
            left += 1

        return res
