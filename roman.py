def romanToInt(s):
    """
    Given a roman numeral, convert it to an integer.

    >>> romanToInt("MCMXCIV")
    1994
    >>> romanToInt("LVIII")
    58
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D': 500,'M':1000}
    num = 0
    
    for idx, x in enumerate(s):
        value = roman_dict.get(x)
        minus = 0
        if idx == 0:
            pass
        elif (x == 'V' or x == 'X') and s[idx-1] == 'I':
            minus = 1
            num -= 1
        elif (x == 'L' or x == 'C') and s[idx-1] == 'X':
            minus = 10
            num -= 10
        elif (x == 'D' or x == 'M') and s[idx-1] == 'C':
            minus = 100
            num -= 100
         
        num += value - minus
        # print(f'x is {x}, minus is {minus}, num is {num}')   
    return num

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')