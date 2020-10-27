def decompressRLElist(nums):
    """
    >>> decompressRLElist([1,2,3,4])
    [2, 4, 4, 4]
    """
    ret = []
    nums = [nums[i:i + 2] for i in range(0, len(nums), 2)] 
 
    for pair in nums:
        ret.append([pair[1] for i in range(pair[0])])
    return [item for sublist in ret for item in sublist]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')