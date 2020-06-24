# 정수 수열


def matrix_mul(x, y, size=2):
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            mat[i][j] = sum(x[i][k] * y[k][j] for k in range(size)) % 100
    return mat


def matrix_dc_pow(mat, e, size=2):
    val = [[1 if i == j else 0 for i in range(size)] for j in range(size)]
    while e:
        val = matrix_mul(mat, val, size) if e % 2 else val
        mat = matrix_mul(mat, mat, size)
        e //= 2
    return val


x, y, a0, a1, n = map(int, input().split())
if n > 1:
    t = matrix_dc_pow([[x, y], [1, 0]], n-1)
    ans = str((a1 * t[0][0] + a0 * t[0][1]) % 100)
else:
    ans = str(a1 if n else a0)

print(ans if len(ans)-1 else '0'+ans)