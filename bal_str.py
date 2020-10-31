def balancedStringSplit(s):
    """
    Balanced strings are those who have equal quantity of 'L' and 'R' characters.
    Given a balanced string s split it in the maximum amount of balanced strings.
    Return the maximum amount of splitted balanced strings.

    >>> balancedStringSplit("RLRRLLRLRL")
    4
    >>> balancedStringSplit("RLLLLRRRLR")
    3
    """
    balanced = 0
    ret = 0
    for char in s:
        if char == 'R':
            balanced += 1
        elif char == 'L':
            balanced -= 1
        if balanced == 0:
            ret += 1
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')