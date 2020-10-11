def findTheDistanceValue(arr1, arr2, d):
    """
    Given two integer arrays arr1 and arr2, and the integer d, return the distance 
    value between the two arrays. The distance value is defined as the number of 
    elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

    >>> findTheDistanceValue([4,5,8], [10,9,1,8], 2)
    2
    >>> findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6)
    1
    """
    count = 0
    
    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                break
        else:
            count +=1
    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')