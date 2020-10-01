def sortedSquares(A):
    """
    Given an array of integers A sorted in non-decreasing order, return an array 
    of the squares of each number, also in sorted non-decreasing order.

    >>> sortedSquares([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]

    >>> sortedSquares([-7,-3,2,3,11])
    [4, 9, 9, 49, 121]
    """
    return sorted([num * num for num in A])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
