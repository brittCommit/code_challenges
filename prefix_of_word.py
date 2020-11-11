def isPrefixOfWord(sentence, searchWord):
    """
    Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
    If searchWord is a prefix of more than one word, return the index of the first word (minimum index). 
    If there is no such word return -1.
    A prefix of a string S is any leading contiguous substring of S.
    
    >>> isPrefixOfWord("i love eating burger", "burg")
    4
    >>> isPrefixOfWord("this problem is an easy problem", "pro")
    2
    """
    sentence = sentence.split()
    
    for idx, word in enumerate(sentence):
        if word.startswith(searchWord):
            return idx + 1
    return -1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')