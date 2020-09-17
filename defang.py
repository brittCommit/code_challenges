def defangIPaddr(address):
    ret = ''
    for char in address:
        if char == '.':
            ret += "[.]"
        else:
            ret += char
    return ret
                

def defangIPaddr(address):
    """Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]". eturn address.replace(".", "[.]")

    >>> defangIPaddr(address = "1.1.1.1")
    '1[.]1[.]1[.]1'
    """
    return address.replace(".", "[.]")
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')