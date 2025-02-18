class MinimumRecolors:
    """
    2379. Minimum Recolors to Get K Consecutive Black Blocks
    https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Approach:
            - Use a fixed window with size `k` to track the number of white blocks in the window, denote as `cur`
            - The minimum recolor operations is the minimum of `cur`
        TC: O(N)
        SC: O(1)
        """
        minimum = len(blocks)
        left = cur = 0

        for right, block in enumerate(blocks):
            if block == "W":
                cur += 1

            if right - left + 1 < k:
                continue

            minimum = min(minimum, cur)

            if blocks[left] == "W":
                cur -= 1
            left += 1

        return minimum
