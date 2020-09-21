def sortArrayByParityII(A):
    """
    Given an array A of non-negative integers, half of the integers in A are odd, 
    and half of the integers are even.Sort the array so that whenever A[i] is odd, 
    i is odd; and whenever A[i] is even, i is even. You may return any answer 
    array that satisfies this condition.

    >>> sortArrayByParityII([4,2,5,7])
    [4,7,2,5], [2,5,4,7], [2,7,4,5] or [4,5,2,7]
    """
    
    odds = []
    evens = []
    ret = []
    
    for num in A:
        if num%2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    while len(odds) > 0:
        ret.append(evens.pop())
        ret.append(odds.pop())
    return ret