# https://atcoder.jp/contests/abc116/tasks/abc116_b
s = int(input())
memo = [0 for _ in range(10 ** 6 + 1)]
memo[s] = True
counter = 1
while True:
    if s % 2 == 0:
        s = s // 2
        counter += 1
        if memo[s]:
            print(counter)
            exit()
        else:
            memo[s] = True
    else:
        s = 3 * s + 1
        counter += 1
        if memo[s]:
            print(counter)
            exit()
        else:
            memo[s] = True
