class LongestPalindrome:
    """
    Problem:    409. Longest Palindrome
    Link:       https://leetcode.com/problems/longest-palindrome/description/
    """

    def longestPalindrome(self, s: str) -> int:
        """
        Approach:   longest palindrom must be oven letters + one odd
                    1. Use a map track all letter's frequences.
                    2. Use all oven letters.
                    3. Use all oven part of an odd lettes.
                    3. res + 1
        """
        record = {}
        for c in s:
            record[c] = record.get(c, 0) + 1

        res = 0
        isOddExist = False
        for v in record.values():
            if v % 2 == 0:
                res += v
            else:
                isOddExist = True
                res += v - 1
        if isOddExist:
            return res + 1
        return res
