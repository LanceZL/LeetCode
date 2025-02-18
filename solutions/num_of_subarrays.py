from typing import List


class NumOfSubarrays:
    """
    1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
    https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
    """

    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        """
        Approach:
            - Translate the threshold to threshold * k,
            - Use a fixed window to maintain the sum of `k` elements.
            - Move the window accross the array, update the count whenever the sum meets or exceeds `threshold`
        TC: O(N) as we iterate through the array once
        SC: O(1) Only a few variables are used, independent of input size.
        """
        # egde case
        if threshold == 0:
            return len(nums) - k + 1

        threshold = threshold * k
        left = cnt = cur_sum = 0

        for right, num in enumerate(nums):
            cur_sum += num

            if right - left + 1 < k:
                continue

            if cur_sum >= threshold:
                cnt += 1

            cur_sum -= nums[left]
            left += 1

        return cnt
