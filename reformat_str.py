def reformat(s):
    """
    Find a permutation of the string where no letter is followed by another 
    letter and no digit is followed by another digit. That is, no two adjacent 
    characters have the same type.
    """
    alph = []
    num = []   
    ret = ''
    
    if s.isnumeric() and len(s) > 1 or s.isalpha() and len(s) > 1:
        return ''
    else:
        for char in s:
            if char.isalpha():
                alph.append(char)
            else:
                num.append(char)          
    if len(alph) == len(num):
        while alph or num:
            ret += alph.pop()
            ret += num.pop()
    elif len(alph) > len(num):
        while alph or num:
            if len(alph) == 1:
                ret += alph.pop()
            else:
                ret += alph.pop()
                ret += num.pop()
    else:
        while alph or num:
            if len(num) == 1:
                ret += num.pop()
            else:
                ret += num.pop()
                ret += alph.pop()
    return ret          
