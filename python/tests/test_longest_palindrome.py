from python.solutions.longest_palindrome import LongestPalindrome
from python.utils.test_case import Case


def test_longest_palindrome():
    """
    Tests for 409. Longest Palindrome.
    """
    cases = [
        Case(params="abccccdd", expect=7),
        Case(params="aaaaaaaa", expect=8),
        Case(params="abc", expect=1),
        Case(params="abcdaab", expect=5),
        Case(
            params="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth",
            expect=983,
        ),
    ]

    for testcase in cases:
        assert LongestPalindrome().longestPalindrome(testcase.params) == testcase.expect
