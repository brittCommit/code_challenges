def largeGroupPositions(s):
    """
    >>> largeGroupPositions("aaa")
    [[0, 2]]

    >>> largeGroupPositions("abbxxxxzzy")
    [[3, 6]]

    """
    ret = []
    count = 0
    current_char = s[0]
    i = 0
    
    for idx, x in enumerate(s):
        if x == current_char:
            count += 1
            if idx == len(s)-1 and count >=3:
                ret.append([i, (i + count-1)])
        elif x != current_char:
            if count >= 3:
                ret.append([i, (i + count-1)])
            count = 1
            current_char = x
            i = idx
    return ret   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')