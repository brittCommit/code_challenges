import statistics
def findSpecialInteger(arr):
    """
    Given an integer array sorted in non-decreasing order, there is exactly one 
    integer in the array that occurs more than 25% of the time. Return that integer.

    >>> findSpecialInteger([1,2,2,6,6,6,6,7,10])
    6

    >>> findSpecialInteger([3, 3, 7, 7, 7, 7, 7])
    7
    """
    return statistics.mode(arr)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
