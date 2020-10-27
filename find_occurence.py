def findOcurrences(text, first, second):
    """
    Given words first and second, consider occurrences in some text of the form 
    "first second third", where second comes immediately after first, and third 
    comes immediately after second.
    For each such occurrence, add "third" to the answer, and return the answer.

    >>> findOcurrences("alice is a good girl she is a good student", "a", "good")
    ['girl', 'student']

    >>> findOcurrences("we will we will rock you", "we", "will")
    ['we', 'rock']
    """
    ret = []
    text = text.split(' ')
    
    for i, word in enumerate(text):
        if i == len(text) -2:
            break
        if word  == first and text[i+1] == second:
            ret.append(text[i+2])
    return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')