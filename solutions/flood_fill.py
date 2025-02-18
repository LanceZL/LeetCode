from typing import List


class FloodFill:
    """
    Problem:733. Flood Fill
    Link:   https://leetcode.com/problems/flood-fill/description/
    """

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        Approach:   Employ a dfs to tackle this problem.
                    Mark any adjecent block with the given color when iterating over the image.
                    Skip a block if it is either out of the boundary, already marked, or not the same coler as the original one.
        TC:         O(MN)
        SC:         O(MN)
        """
        m, n = len(image), len(image[0])
        visited = [[False] * n for i in range(m)]

        self.dfs(image, visited, sr, sc, color, image[sr][sc])

        return image

    def dfs(
        self,
        image: List[List[int]],
        visited: List[List[bool]],
        r: int,
        c: int,
        color: int,
        original: int,
    ):
        """Helper DFS function."""
        # Out of boundray or meets a blocker or already been visited.
        is_out_boundary = r < 0 or c < 0 or r >= len(image) or c >= len(image[0])
        if is_out_boundary or visited[r][c] or image[r][c] != original:
            return

        image[r][c] = color
        visited[r][c] = True

        self.dfs(image, visited, r + 1, c, color, original)
        self.dfs(image, visited, r - 1, c, color, original)
        self.dfs(image, visited, r, c + 1, color, original)
        self.dfs(image, visited, r, c - 1, color, original)
