def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


# ax + by = gcd(a, b)
# returns (x, y, gcd(a, b))
def ext_gcd(a: int, b: int) -> tuple:
    if b == 0:
        return 1, 0, a
    q, r = a // b, a % b
    x, y, g = ext_gcd(b, r)
    s, t = y, x - q * x
    return s, t, g


if __name__ == '__main__':
    print(gcd(1414, 154))
    print(ext_gcd(0, 3))
    print(ext_gcd(1414, 154))
    print(ext_gcd(4, 12))
