import math


def isPowerOfTwo(n):
    """Given an integer, write a function to determine if it is a power of two.
    >>> isPowerOfTwo(1)
    True
    >>> isPowerOfTwo(16)
    True
    >>> isPowerOfTwo(218)
    False
    """

    return n>0 and math.log2(n)%1==0

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')