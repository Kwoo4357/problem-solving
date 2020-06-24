# 본대 산책 3


def matrix_mul(x, y, size=2):
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            mat[i][j] = sum(x[i][k] * y[k][j] for k in range(size)) % (10 ** 9 + 7)
    return mat


def matrix_dc_pow(mat, e, size=2):
    val = [[1 if i == j else 0 for i in range(size)] for j in range(size)]
    while e:
        val = matrix_mul(mat, val, size) if e % 2 else val
        mat = matrix_mul(mat, mat, size)
        e //= 2
    return val


n, m = map(int, input().split())
build = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    build[a-1][b-1] = 1
    build[b-1][a-1] = 1

print(matrix_dc_pow(build, int(input()), n)[0][0])
