def maximum69Number (num):
    """
    Given a positive integer num consisting only of digits 6 and 9.Return the 
    maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
    
    >>> maximum69Number(9669)
    9969

    >>> maximum69Number(9999)
    9999

    """
    if '6' not in str(num):
        return int(num)
  
    max_num = num
    for n in str(num):
        if n == str('9'):
            pass
        else:
            new_num = (str(num).replace('6','9',1))
            if int(new_num) > max_num:
                max_num = int(new_num)
            return max_num

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')