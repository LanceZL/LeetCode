from typing import List


class TwoSum:
    """
        Problem:    001. Two sum
        Link:       https://leetcode.com/problems/two-sum/description/
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {value: index}
        record = {}

        for i, v in enumerate(nums):
            if target - v in record:
                return [record[target - v], i]
            record[v] = i

        return [-1, -1]
    