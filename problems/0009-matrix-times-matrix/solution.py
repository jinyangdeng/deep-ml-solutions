def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a_0, a_1 = len(a), len(a[0])
    b_0, b_1 = len(b), len(b[0])
    if a_1 != b_0:
        return -1

    b_tranpose =  [list(col) for col in zip(*b)]
    res = [[0] * b_1 for _ in range(a_0)]
    for rowIdx, row in enumerate(a):
        for colIdx, col in enumerate(b_tranpose):
            res[rowIdx][colIdx] = sum(rr * cc for rr, cc in zip(row, col))
    return res