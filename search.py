def search(nums, target):
    """
    Given a sorted (in ascending order) integer array nums of n elements and a 
    target value, write a function to search target in nums. If target exists, 
    then return its index, otherwise return -1.
    
    >>> search([-1,0,3,5,9,12], 9)
    4
    >>> search([-1,0,3,5,9,12], 2)
    -1
    """
    return nums.index(target) if target in nums else -1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')