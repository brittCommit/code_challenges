from collections import Counter
import re

def mostCommonWord(paragraph, banned):    
    """
    Given a paragraph and a list of banned words, return the most frequent word 
    that is not in the list of banned words.  It is guaranteed there is at least 
    one word that isn't banned, and that the answer is unique.

    Words in the list of banned words are given in lowercase, and free of punctuation.  
    Words in the paragraph are not case sensitive.  The answer is in lowercase.
    
    >>> mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    'ball'
    """
    paragraph = paragraph.lower()
    paragraph = re.split("\W+", paragraph)
    word_dict = Counter(paragraph)
    found = False
    
    while not found:
        x = word_dict.most_common(1)
        word = x[0][0]
        if not word.isalpha():
            word_dict.pop(word)
        if word in banned:
            word_dict.pop(word)
        else:
            found = True
            return word.lower()

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
