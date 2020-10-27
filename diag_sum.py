def diagonalSum(mat):
    """
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the 
    elements on the secondary diagonal that are not part of the primary diagonal.

    >>> diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
    25
    """
    total = 0
        
    n = len(mat)
    for i in range(0, n):  
        for j in range(0, n):  
            if (i == j): 
                total += mat[i][j] 
            elif ((i + j) == (n - 1)): 
                total += mat[i][j]
    return total

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')