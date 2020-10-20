def selfDividingNumbers(left, right):
    """
    Given a lower and upper number bound, output a list of every possible 
    self dividing number, including the bounds if possible.
    A self-dividing number is a number that is divisible by every digit it contains.
    >>> selfDividingNumbers(1, 22)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    """
    ret = []
    bounds = list(range(left, right + 1))
    
    for num in bounds:
        div = True
        if '0' in str(num):
            pass
        elif num < 10:
            ret.append(num)
        else:
            for n in str(num):     
                if num % int(n) !=0:
                    div = False
            if div is True:
                ret.append(num)    
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')