"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""

def is_palindrome(dictionary):
    """Do the letter counts in a dictionary make a palindrome"""

    odd_letter = 0
    
    for value in dictionary.values():
        if value % 2 == 1:
            odd_letter += 1
    return odd_letter == 1

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_count_dict = {}

    if len(word) % 2 == 0:
        return False
    elif len(word) == 1:
        return True
    else:
        for letter in word:
            if letter not in letter_count_dict:
                letter_count_dict[letter] = 1
            else:
                letter_count_dict[letter] += 1
    return is_palindrome(letter_count_dict)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
