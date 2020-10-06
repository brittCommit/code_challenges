def majorityElement(nums):
    """
    Given an array of size n, find the majority element. The majority element is the 
    element that appears more than ⌊ n/2 ⌋ times. You may assume that the array is 
    non-empty and the majority element always exist in the array.

    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """
    return mode(nums)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')