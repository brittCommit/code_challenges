def reformatDate(date):
    """
    Convert the date string to the format YYYY-MM-DD.

    >>> reformatDate("20th Oct 2052")
    '2052-10-20'

    >>> reformatDate("6th Jun 1933")
    '1933-06-06'
    """
    month_dict = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05',                       "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct":                            '10',"Nov": '11', "Dec": '12'}
    
    month = date[5:8] if len(date) == 13 else date[4:7]
    year = date[-4:]
    day = date[:2] if len(date) == 13 else '0' + date[:1]

    return year+'-'+(month_dict[month])+'-'+day

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')