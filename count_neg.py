def countNegatives(grid):
    """
    Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
    Return the number of negative numbers in grid.
    >>> countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> countNegatives([[3,2],[1,0]])
    0
    """
    count = 0
    for num in grid:
        for n in num:
            if n < 0:
                count += 1
    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')