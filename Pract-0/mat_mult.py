def matrix_multiply(A, B):
    m = len(A)  
    n = len(A[0])   
    p = len(B[0])

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = matrix_multiply(A, B)
for row in result:
    print(row)
