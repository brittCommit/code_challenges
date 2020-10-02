def countOdds(low, high):
    """
    Given two non-negative integers low and high. 
    Return the count of odd numbers between low and high (inclusive).
    >>> countOdds(3, 7)
    3
    >>> countOdds(8, 10)
    1
    """
    
    return ((high - low +1)// 2) if high % 2 == 0 or low % 2 == 0 else ((high - low)// 2) + 1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')