def distributeCandies(candies):
    """
    You have n candies, the ith candy is of type candies[i].You want to distribute 
    the candies equally between a sister and a brother so that each of them 
    gets n / 2 candies (n is even). The sister loves to collect different types of 
    candies, so you want to give her the maximum number of different types of candies.
    Return the maximum number of different types of candies you can give to the sister.
    
    >>> distributeCandies([1,1,2,2,3,3])
    3
    >>> distributeCandies([1,1,2,3])
    2
    >>> distributeCandies([1,1])
    1
    """
    sister = set()
    
    for int in candies:
        sister.add(int)
    
    if len(sister) <= len(candies)/2:
        return len(sister)
    else:
        return len(candies)//2

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')