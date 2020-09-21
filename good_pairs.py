def numIdenticalPairs(nums):
    """A pair (i,j) is called good if nums[i] == nums[j] and i < j. 
    Return the number of good pairs.

    >>> numIdenticalPairs([1,2,3,1,1,3])
    4

    >>> numIdenticalPairs([1,1,1,1])
    6

    >>> numIdenticalPairs([1,2,3])
    0
    """

    ret = 0
    
    while len(nums) > 0:
        for idx, num in enumerate(nums):
            if idx == 0:
                i = num
            elif i == num:
                ret += 1
        nums = nums[1:]
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')