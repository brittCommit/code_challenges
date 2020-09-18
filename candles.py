def kidsWithCandies(candies, extraCandies):
    """Given the array candies and the integer extraCandies, 
    where candies[i] represents the number of candies that the ith kid has.
    For each kid check if there is a way to distribute extraCandies among the 
    kids such that he or she can have the greatest number of candies among them.

    >>> kidsWithCandies([2,3,5,1,3], 3)
    [True, True, True, False, True]

    >>> kidsWithCandies([4,2,1,1,2], 1)
    [True, False, False, False, False]
    """

    most = max(candies)
    ret = []

    for kid in candies:
        if (kid + extraCandies) >= most:
            ret.append(True)
        else:
            ret.append(False)
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')