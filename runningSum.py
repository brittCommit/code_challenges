def runningSum(nums):
    """Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.

    >>> runningSum([1, 2, 3, 4])
    [1, 3, 6, 10]

    >>> runningSum([1, 1, 1, 1, 1])
    [1, 2, 3, 4, 5]

    >>> runningSum([3, 1, 2, 10, 1])
    [3, 4, 6, 16, 17]
    """
    
    ret = []
    for idx, num in enumerate(nums):
        if idx == 0:
            ret.append(num)
        else:
            ret.append(num + ret[idx - 1]) 
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')