import math

def mySqrt(x):
    """Return the square root in a whole number of a given number.

    >>> mySqrt(8)
    2

    >>> mySqrt(4)
    2

    >>> mySqrt(0)
    0
    """

    return int(math.sqrt(x))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')