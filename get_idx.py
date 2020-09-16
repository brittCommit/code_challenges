def get_indices(num_list, target):
    """Return indices of the two numbers such that they add up to target.

    >>> get_indices([2,7,11,15],9) 
    [0, 1]

    >>> get_indices([3,3], 6)
    [1, 0]

    >>> get_indices([3,2,4], 6)
    [1, 2]
    """

    for idx, num in enumerate(num_list):
        diff = target - num
        if diff in num_list and num_list.index(diff) != idx:
          return [idx, num_list.index(diff)]
    return ("Cannot find target")

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')