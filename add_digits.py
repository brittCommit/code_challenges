def addDigits(num): 
    """
    Given a non-negative integer num, repeatedly add all its digits until 
    the result has only one digit.

    >>> addDigits(38)
    2
    """
    while num > 9:
        num = sum([int(x) for x in str(num)])
    return num

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')