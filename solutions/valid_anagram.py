class ValidAnagram:
    """
    Problem:    242. Valid Anagram
    Link:       https://leetcode.com/problems/valid-anagram/description/
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach:   1. Create an array to keep track of the frequency of each character in string s.
                    2. Iterate through string t and decrease the frequency for each character found in t.
                    3. If t is an anagram of s, all frequencies in the array should be zero by the end of the iteration.
        TC:         O(N)
        SC:         O(26)
        """
        record = [0] * 26  # Init a record
        # record the frequencies in s
        for letter in s:
            record[ord(letter) - ord("a")] += 1

        # Iterate t, decreae the frequence
        for letter in t:
            record[ord(letter) - ord("a")] -= 1

        # Check if it's an anagram
        for f in record:
            if f != 0:
                return False
        return True
