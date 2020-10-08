from collections import Counter
def uniqueOccurrences(arr):
    """
    Given an array of integers arr, write a function that returns true if and 
    only if the number of occurrences of each value in the array is unique.

    >>> uniqueOccurrences([1,2,2,1,1,3])
    True
    >>> uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    True
    >>> uniqueOccurrences([1,2])
    False
    """

    dict = Counter(arr)
    unique = set()
    
    for key, value in dict.items():
        if value in unique:
            return False
        else:
            unique.add(value)
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')