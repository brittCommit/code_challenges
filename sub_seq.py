def minSubsequence(nums):
    """
    Given the array nums, obtain a subsequence of the array whose sum of elements 
    is strictly greater than the sum of the non included elements in such subsequence. 
    
    >>> minSubsequence([4,3,10,9,8])
    [10, 9]
    >>> minSubsequence([4,4,7,6,7])
    [7, 7, 6]
    """
    ret = []
    tot = sum(nums)
    
    for num in reversed(sorted(nums)):
        ret.append(num)
        if sum(ret) > tot//2:
            return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')