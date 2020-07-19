"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    #loop over every character of the string
    #count characters while looping
    #when character limit is hit insert new line
        #how to account for when character hits in the middle of the word?
    #start count over
    
    if len(string) <= limit:
        print(string)

    
    else:

        char_count = 0
        word_list = string.split()
        new_string=''

        for word in word_list:
            if limit - char_count >= len(word):
                new_string += word + ' ' 
                char_count += len(new_string)

            else:
                print(new_string)
                
                char_count = 0
                new_string = ''
                new_string += word + ' '
                char_count += len(new_string)
        print(new_string)

        # for char in string:
        #     char_count += 1
        #     new_string += char

        #     if char_count == limit:
        #         print(new_string)
        #         char_count = 0
        #         new_string = ' '
        #         '\n'



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
