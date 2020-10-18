from collections import Counter
def numJewelsInStones(J, S):
    """
    >>> numJewelsInStones("z", "ZZ")
    0
    >>> numJewelsInStones("aA", "aAAbbbb")
    3
    """
    stone_count = Counter(S)
    ret = 0
    
    for jewel in J:
        if jewel in stone_count:
            ret += stone_count[jewel]
    
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')