def strStr(haystack, needle):
    """Return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.

    >>> strStr("hello", "ll")
    2

    >>> strStr("mississippi", "issip")
    4

    >>> strStr("a", "")
    0
    """

    if not needle in haystack:
        return -1
    elif len(haystack) == 0 or len(needle) == 0:
        return 0
    else:
        return haystack.index(needle)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')