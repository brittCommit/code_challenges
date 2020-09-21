def thousandSeparator(n):
    """
    Given an integer n, add a dot (".") as the thousands separator and return it in string format.

    >>> thousandSeparator(123456789)
    "123.456.789"

    >>> thousandSeparator(987)
    "987"

    >>> thousandSeparator(1234)
    "1.234"
    """

    n = str(n)
    ret = ''
    if len(n) < 4:
        return str(n) 
    if len(n)%3 == 1:
        ret = n[0] + "."
        n = n[1:]
    if len(n)%3 == 2:
        ret = n[0] + n[1] + "."
        n = n[2:]
    for idx, num in enumerate(n):
        if idx%3 == 0 and idx > 0:
            ret = ret + "." + num
        else:
            ret = ret + num     
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')