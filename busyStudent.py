"""Return the number of students that were working during the queryTime.

    >>> busyStudent([9,8,7,6,5,4,3,2,1],[10,10,10,10,10,10,10,10,10],10)
    9

    >>> busyStudent([1,1,1,1], [1,3,2,4], 7)
    0

    >>> busyStudent([1,2,3], [3,2,7], 4)
    1
"""

def busyStudent(startTime, endTime, queryTime):    
        
    #for each student in start time, check if value is < > query time
    #add 1 to return value if true
    # i = index

    i = 0

    output = 0
    
    while i <= len(startTime) - 1:
        if queryTime in range(startTime[i], endTime[i]+1):
            output += 1
        i += 1
        
    return output

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')