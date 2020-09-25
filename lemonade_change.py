def lemonadeChange(bills):
    """At a lemonade stand, each lemonade costs $5. 
    Customers are standing in a queue to buy from you, and order one at a time 
    (in the order specified by bills). Each customer will only buy one lemonade 
    and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer,
    so that the net transaction is that the customer pays $5.Note that you don't have any change in hand at first.
    Return true if and only if you can provide every customer with correct change.

    >>> lemonadeChange([5,5,5,10,20])
    True

    >>> lemonadeChange([5,5,10])
    True

    >>> lemonadeChange([5,5,10,10,20])
    False

    >>> lemonadeChange([10, 5])
    False
    """
    bank = {5: 0, 10: 0, 20: 0}

    if bills[0] != 5:
        return False
    
    for bill in bills:
        bank[bill] += 1
        if bill == 10:
            bank[5] -= 1
            if bank[5] < 0: 
                return False
        if bill == 20:
            if bank[10] >= 1 and bank[5] >= 1:
                bank[10] -= 1
                bank[5] -= 1
            elif bank[5] >= 3:
                bank[5] -=3
            else:    
                return False         
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')