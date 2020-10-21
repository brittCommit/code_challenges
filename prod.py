import numpy
def subtractProductAndSum(n):
    """
    Given an integer number n, return the difference between the product of 
    its digits and the sum of its digits.

    >>> subtractProductAndSum(234)
    15
    >>> subtractProductAndSum(4421)
    21
    """
    digs = [int(num) for num in str(n)]
    return numpy.prod(digs) - sum(digs)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')