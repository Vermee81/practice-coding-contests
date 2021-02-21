if __name__ == '__main__':
    def modpow(a, n, mod):
        res = 1
        while n > 0:
            if n & 1:
                res = res * a % mod
            a = a * a % mod
            n >>= 1
        return res


    def modinv(a: int, m: int) -> int:
        return modpow(a, m - 2, m)

    a1, b1, x1 = [0, 5, 1]
    counter = 0
    MOD = 10 ** 9 + 7
    b1_inv = modinv(x1, MOD)

    for i in range(a1, b1 + 1):
        i_i = i % MOD
        hogehoge = (i_i * b1_inv)
        hogehoge_mod = hogehoge % MOD
        wari = hogehoge_mod
        # wari = ((i_i * b1_inv) % MOD) % x1
        if wari == 0:
            counter += 1
    print(counter)
