import math
def smallest_subarray_with_given_sum(s, arr):
    """Given an array of positive numbers and a positive number ‘S,’ find the 
    length of the smallest contiguous subarray whose sum is greater than or equal 
    to ‘S’. Return 0 if no such subarray exists.
    >>> smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])
    2
    >>> smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])
    3
    """
    window_sum, window_start = 0, 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0    
    return min_length

def max_sub_array_of_size_k(k, arr):
    """
    Given an array of positive numbers and a positive number ‘k,’ 
    find the maximum sum of any contiguous subarray of size ‘k’.

    >>> max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
    9
    >>> max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
    7
    """
    w_sum, w_start, max_sum = 0, 0, 0

    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        if w_end >= k-1:
            max_sum = max(max_sum, w_sum)
            w_sum -= arr[w_start]
            w_start += 1
    return max_sum

def longest_substring_with_k_distinct(str, k):
    """
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    >>> longest_substring_with_k_distinct("araaci", 2)
    4
    >>> longest_substring_with_k_distinct("cbbebi", 3)
    5
    """
    w_start, max_length = 0,0
    char_frequency = {}

    for w_end in range(len(str)):
        right_char = str[w_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str[w_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            w_start += 1
        max_length = max(max_length, w_end-w_start +1)
    return max_length

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')