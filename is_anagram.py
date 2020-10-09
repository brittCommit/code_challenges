from collections import Counter

def isAnagram(s, t):
    """
    Given two strings s and t , write a function to determine if t is an anagram of s.
    >>> isAnagram("anagram", "nagaram")
    True
    >>> isAnagram("rat", "car")
    False
    """
    return Counter(s) == Counter(t)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')