def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    M, N = len(matrix), len(matrix[0])
    for i in range(M):
        for j in range(N):
            matrix[i][j] *= scalar
    
    return matrix
    