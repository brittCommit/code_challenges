def replaceElements(arr):
    """
    Given an array arr, replace every element in that array with the greatest 
    element among the elements to its right, and replace the last element with -1.

    >>> replaceElements([17,18,5,4,6,1])
    [18, 6, 6, 6, 1, -1]
    """
    ret = []
    
    for i, num in enumerate(arr):
        if i + 1 == len(arr):
            ret.append(-1)
            return ret
        else:
            new_arr = arr[i+1:]
            ret.append(max(new_arr))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')