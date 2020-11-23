def mutateTheArray(n, a):
    """
    Given an integer n and an array a of length n, your task is to apply the following mutation to a:

    Array a mutates into a new array b of length n.
    For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
    If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].

    >>> mutateTheArray (5, [4, 0, 1, -2, 3])
    [4, 5, -1, 2, 1]

    """
    if n < 2:
        return a
    b = []
    
    for i in range(len(a)):
        if i == 0:
            b.append((a[i] + a[i+1]))
        elif i == (len(a)-1):
            b.append((a[i] + a[i-1]))
        else:
            b.append((a[i-1] + a[i] + a[i+1]))
    return b

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')