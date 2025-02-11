class RansomNote:
    """
    Problem:    383. Ransom Note
    Link:       https://leetcode.com/problems/ransom-note/description/
    """

    def canConstruct(self, s1: str, s2: str) -> bool:
        """
        Approach:   1.Create a array to keep track of the frequency of each letters in s2.
                    2.Decrease the frequecy for letters found in when iterating s1.
                    3.All frequencies should equal or greater than 0 if s1 can be contructed by s2.
        TC:         O(1)
        SC:         O(1)
        """
        record = [0] * 26

        for letter in s2:
            record[ord(letter) - ord("a")] += 1

        for letter in s1:
            record[ord(letter) - ord("a")] -= 1

        for f in record:
            if f < 0:
                return False
        return True
