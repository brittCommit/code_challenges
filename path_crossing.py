def isPathCrossing(path):
    """
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing 
    moving one unit north, south, east, or west, respectively. You start at the 
    origin (0, 0) on a 2D plane and walk on the path specified by path.

    Return True if the path crosses itself at any point, that is, if at any time 
    you are on a location you've previously visited. Return False otherwise.

    >>> isPathCrossing("NES")
    False
    >>> isPathCrossing("NESWW")
    True
    """
    history = [(0,0)]
    for d in path:
        v = history[-1][0]
        h = history[-1][1]
        if d == 'N':
            new_c = (v + 1, h)   
        if d == 'S':
            new_c = (v - 1, h)
        if d == 'E':
            new_c = (v, h - 1)
        if d == 'W':
            new_c = (v, h + 1)
        if new_c in history:
                return True
        history.append(new_c)
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')