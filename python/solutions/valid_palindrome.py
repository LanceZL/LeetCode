class ValidParlindrome:
    """
    Problem : 125. Valid Palindrome
    Link    : https://leetcode.com/problems/valid-palindrome/description/
    """

    def isPalindrome(self, s: str) -> bool:
        """
        Solution    : Employ a two-pointer approach to tackle this problem.
        TC          : O(N)
        SC          : O(1)
        """
        n = len(s)
        if n <= 1:  # Corner Case
            return True
        s = s.lower()
        left, right = 0, n - 1  # two pointers
        while left < right:
            # Skip non-alphanumeric charaters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare two pointers
            if left < right and s[left] != s[right]:
                return False

            # Move two pointers towards each other
            left += 1
            right -= 1

        return True
