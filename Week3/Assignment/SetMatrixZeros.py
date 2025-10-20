matrix1 = [[1,1,1],
          [1,0,1],
          [1,1,1]]
matrix2 = [[0,1,2,0],
           [3,4,5,2],
           [1,3,1,5]]

def SetMatrixZeros(matrix):
    # store whether col0/row0 have 0
    # if 0, col0/row0 is True
    m = len(matrix)
    n = len(matrix[0])
    col0 = any(matrix[i][0] == 0 for i in range(m))
    row0 = any(matrix[0][i] == 0 for i in range(n))

    # reset the col0 and row0 as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    # set zeros according to the markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # reset the row0 and col0
    if row0:
        for i in range(n):
            matrix[0][i] = 0
    if col0:
        for i in range(m):
            matrix[i][0] = 0

SetMatrixZeros(matrix1)
SetMatrixZeros(matrix2)

print(matrix1)
print(matrix2)

