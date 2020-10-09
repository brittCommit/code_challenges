def sortArrayByParity(A):
    """
    Given an array A of non-negative integers, return an array consisting of 
    all the even elements of A, followed by all the odd elements of A.
    """
    even = []
    odd = []
    
    for idx, i in enumerate(A):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd
                