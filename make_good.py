def makeGood(s):
    """
    >>> makeGood("leEeetcode")
    'leetcode'
    """
    if len(s) < 2:
        return s
    
    i = 0
    while i < (len(s) -1):
        x = s[i]
        y = s[i+1]
        if x == y: 
            i += 1
        elif x.lower() == y.lower():
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1  
    return s

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')