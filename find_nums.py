def findNumbers(nums):
    """
    Given an array nums of integers, return how many of them contain an even number of digits.
    >>> findNumbers([12,345,2,6,7896])
    2
    >>> findNumbers([555,901,482,1771])
    1
    """
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')