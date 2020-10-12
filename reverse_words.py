def reverseWords(s):
    """
    Given a string, you need to reverse the order of characters in each word 
    within a sentence while still preserving whitespace and initial word order.

    >>> reverseWords("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"
    """
    s = (s).split(' ')
    ret = ''
    
    for word in s:
        ret += ' ' + word[::-1]
    return ret.lstrip()

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')