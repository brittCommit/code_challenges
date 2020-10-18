def smallerNumbersThanCurrent(nums):
    """
    Given the array nums, for each nums[i] find out how many numbers in the array 
    are smaller than it. That is, for each nums[i] you have to count the number of 
    valid j's such that j != i and nums[j] < nums[i].
    
    >>> smallerNumbersThanCurrent([8,1,2,2,3])
    [4, 0, 1, 1, 3]
    >>> smallerNumbersThanCurrent([7,7,7,7])
    [0, 0, 0, 0]
    """
    new_nums = sorted(nums)
    ret = []
    
    for num in nums:
        ret.append(new_nums.index(num))     
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')