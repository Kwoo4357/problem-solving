# Immortal Porpoises


def matrix_mul(x, y, size=2):
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            mat[i][j] = sum(x[i][k] * y[k][j] for k in range(size)) % (10 ** 9)
    return mat


def matrix_dc_pow(mat, e, size=2):
    val = [[1 if i == j else 0 for i in range(size)] for j in range(size)]
    while e:
        val = matrix_mul(mat, val, size) if e % 2 else val
        mat = matrix_mul(mat, mat, size)
        e //= 2
    return val


for _ in range(int(input())):
    k, y = map(int, input().split())
    print(k, matrix_dc_pow([[1, 1], [1, 0]], y)[1][0])