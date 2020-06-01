# random number generator
def geometric(r, n, m):
    T = 1
    an = r % m
    total = 0
    while n:
        total = (an * total + T) % m if n & 1 else total
        T = ((an + 1) * T) % m
        an = an ** 2 % m
        n //= 2
    return total


m, a, c, x0, n, g = map(int, input().split())
print((pow(a, n, m) * x0 + c * geometric(a, n, m)) % m % g if a > 1 else x0 * a + c * (n - 1) * a + c)
