def toGoatLatin(S):
    """
    >>> toGoatLatin("I speak Goat Latin")
    'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
    """
    S = S.split(' ')
    ret = ''
    
    for i, el in enumerate(S):
        if el[0].lower() in 'aeiou':
            ret += el + 'ma' + 'a'*(i+1) + ' '
        else:
            x = el[:1]
            ret += el[1:] + x + 'ma' + 'a'*(i+1) + ' '
    return ret.rstrip(' ')
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')