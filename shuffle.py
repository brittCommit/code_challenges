def shuffle(nums, n):
    """Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    >>> shuffle([2,5,1,3,4,7],3)
    [2,3,5,4,1,7]

    >>> shuffle([1,2,3,4,4,3,2,1], 4)
    [1,4,2,3,3,2,4,1]

    >>> shuffle([1,1,2,2], 2)
    [1,2,1,2]
    """
    
    #find length of array/2 = n
    #create empty list for output
    #take first element of original list
    #take n element og list
    #increment by 1
    #x index starts at 0
    #y index starts at n

    output = []
    x_idx = 0
    y_idx = n
    
    while nums:
        output.append(nums[0])
        output.append(nums[y_idx])
        nums.pop(y_idx)
        nums.pop(0)
        y_idx -= 1
    return output

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')