from statistics import mean 
def average(salary):
    """
    Given an array of unique integers salary where salary[i] is the salary of the employee i.
    Return the average salary of employees excluding the minimum and maximum salary.
    
    >>> average([4000,3000,1000,2000])
    2500
    >>> average([6000,5000,4000,3000,2000,1000])
    3500
    """
    salary = sorted(salary)
    return mean(salary[1:-1])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')