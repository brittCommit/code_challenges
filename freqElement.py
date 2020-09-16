# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
# then the word with the lower alphabetical order comes first.

from collections import defaultdict, Counter

def freq_el(word_list, i):
    """Given a non-empty list of words, return the k most frequent elements.

    >>> freq_el(['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'],4)
    ['the', 'is', 'sunny', 'day']

    >>> freq_el(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2)
    ['i', 'love']
    """

    #get word counts
    word_counts = Counter(word_list)
    # word_counts = defaultdict(int)
    # for word in word_list:
    #   word_counts[word] += 1

    #Make dictionary with count as key, words with same count as a value in a list
    byfreq = defaultdict(list)
    for k, v in word_counts.items():
        byfreq[v].append(k)

    #sort dictionary by key in decending order, return k items using slicing
    ret = []
    keys = sorted(byfreq, reverse = True)
    for v in keys:
        ret.extend(sorted(byfreq[v]))
    return ret[:i]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')