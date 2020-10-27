def oddCells(n, m, indices):
    """
    Given n and m which are the dimensions of a matrix initialized by zeros and 
    given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] 
    you have to increment all cells in row ri and column ci by 1.
    Return the number of cells with odd values in the matrix after applying the 
    increment to all indices.

    >>> oddCells(2, 3, [[0,1],[1,1]])
    6
    """
    matrix = [[0 for i in range(m)] for j in range(n)]
    negs = 0
    
    for pair in indices:
        ri = pair[0]
        ci = pair[1]
        for i in range(m):
            matrix[ri][i] += 1
        for row in matrix:
            row[ci] +=1
    
    for i in range(m):
        for row in matrix:
            if row[i] % 2 != 0:
                negs +=1
    return negs

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')