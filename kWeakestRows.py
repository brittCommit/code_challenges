def kWeakestRows(mat, k):
    """
    kWeakestRows([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0],[1,1,1,1,1]], 3)
    [2, 0, 3]
    """
    soldiers = {}
    for i, row in enumerate(mat):
        soldiers[i] = 0
        for j in range(len(row)):
            if row[j]  == 1:
                soldiers[i] += 1
    print(soldiers)
    soldiers = sorted(soldiers.items(), key=lambda x: x[1])
    print(soldiers)
    ret = []
    
    for i in soldiers:
        ret.append(i[0])
        if len(ret) == k:
            return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')