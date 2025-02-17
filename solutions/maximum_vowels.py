class MaxVowels:
    """
    Problem:    1456. Maximum Number of Vowels in a Substring of Given Length
    Description: Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
    Link:       https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
    """

    def maxVowels(self, s: str, k: int) -> int:
        """
        Approach: Maintain a fixed window of size k.
            1. Initialize the window and expand the left and right until it reaches the size k
            2. Move the window towards the end.
            3. Calculate and update the maximum.
        TC: O(N) as we iterate over the s once.
        SC: O(1) as we only use a constant number of pointers.
        """
        left = 0
        cur, maximum = 0, 0
        # Init the window
        for right, c in enumerate(s):
            if c in "aeiou":
                cur += 1
            if right - left + 1 < k:
                continue

            maximum = max(maximum, cur)
            if s[left] in "aeiou":
                cur -= 1
            left += 1

        return maximum

    def isVowel(self, c: str) -> bool:
        return c in ["a", "e", "i", "o", "u"]
