def maxProfit(prices):
    """
    Say you have an array prices for which the ith element is the price of a 
    given stock on day i. Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (i.e., buy one and sell 
    one share of the stock multiple times).
    
    >>> maxProfit([7,1,5,3,6,4])
    7
    >>> maxProfit([1,2,3,4,5])
    4
    """
    profit = 0    
    for idx, p in enumerate(prices):
        if idx == 0:
            pass
        elif p > prices[idx -1]:
            profit += p - prices[idx -1]
    return profit

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')