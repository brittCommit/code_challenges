def numberOfSteps(num):
    """
    Given a non-negative integer num, return the number of steps to reduce it 
    to zero. If the current number is even, you have to divide it by 2, otherwise, 
    you have to subtract 1 from it.

    >>> numberOfSteps(14)
    6
    >>> numberOfSteps(8)
    4
    """
    steps = 0
    
    while num != 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num -= 1
            steps += 1
    return steps

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')