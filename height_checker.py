def heightChecker(heights):
    """
    Students are asked to stand in non-decreasing order of heights for an annual photo.
    Return the minimum number of students that must move in order for all students 
    to be standing in non-decreasing order of height.
    >>> heightChecker([5,1,2,3,4])
    5
    >>> heightChecker([1,1,4,2,1,3])
    3
    """
    ordered = sorted(heights)
    moves = 0
    
    for i, h in enumerate(heights):
        if h != ordered[i]:
            moves += 1
    return moves

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')