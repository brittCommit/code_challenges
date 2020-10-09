def containsDuplicate(nums):
    """
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the array, 
    and it should return false if every element is distinct.

    >>> containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    True
    >>> containsDuplicate([1,2,3,1])
    True
    >>> containsDuplicate([1,2,3,4])
    False
    """
    num_check = set()
    
    for num in nums:
        if num in num_check:
            return True
        num_check.add(num)
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')