def peakIndexInMountainArray(arr):
    """
    Let's call an array arr a mountain if the following properties hold:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... arr[i-1] < arr[i]
    arr[i] > arr[i+1] > ... > arr[arr.length - 1]
    Given an integer array arr that is guaranteed to be a mountain, 
    return any i such that:
     arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    >>> peakIndexInMountainArray([0,1,0])
    1
    >>> peakIndexInMountainArray([3,4,5,1])
    2
    >>> peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])
    2

    """
    return arr.index(max(arr))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')