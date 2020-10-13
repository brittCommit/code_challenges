from collections import Counter
def singleNumber(nums):
    """
    Given a non-empty array of integers nums, every element appears twice except 
    for one. Find that single one.
    >>> singleNumber([2,2,1])
    1

    >>> singleNumber([4,1,2,1,2])
    4
    """

    for key, value in Counter(nums).items():
        if value == 1:
            return key

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')