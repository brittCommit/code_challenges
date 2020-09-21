def restoreString(s, indices):
    """Given a string s and an integer array indices of the same length.The string s 
    will be shuffled such that the character at the ith position moves to indices[i] 
    in the shuffled string. Return the shuffled string.

    >>> restoreString("codeleet", [4,5,6,7,0,2,1,3])
    'leetcode'

    >>> restoreString("abc", [0,1,2])
    'abc'

    >>> restoreString("aiohn", [3,1,4,2,0])
    'nihao'
    """
        
    ret = ''
    i = 0
    
    while i < len(indices):
        ret = ret + s[indices.index(i)]
        i += 1
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')