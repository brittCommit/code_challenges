def canMakeArithmeticProgression(arr):  
    """
    Given an array of numbers arr. A sequence of numbers is called an arithmetic progression 
    if the difference between any two consecutive elements is the same.Return true if the array 
    can be rearranged to form an arithmetic progression, otherwise, return false.

    >>> canMakeArithmeticProgression([3,5,1])
    True
 
    >>> canMakeArithmeticProgression([1,2,4])
    False
    """     
    new_arr = sorted(arr)
    diff = new_arr[1] - new_arr[0]
    for idx, num in enumerate(new_arr):
        if idx == 0:
            pass
        elif num - new_arr[idx - 1] != diff:
            return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')