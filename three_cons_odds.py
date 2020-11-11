def threeConsecutiveOdds(arr):
    """
    Given an integer array arr, return true if there are three consecutive odd 
    numbers in the array. Otherwise, return false.

    >>> threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])
    True
    >>> threeConsecutiveOdds([2,6,4,1])
    False
    """
        
    for i in range(len(arr) - 2):
        if arr[i] % 2 != 0 and arr[i +1] % 2 != 0 and arr[i+2] % 2 != 0:
            return True
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')