#등비수열
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


a, r, n, mod = map(int, input().split())
print(a*geometric(r, n, mod)%mod)