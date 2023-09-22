# https://atcoder.jp/contests/abc029/tasks/abc029_c
N = int(input())
moji = ['a', 'b', 'c']


def create(n: int):
    if n == 1:
        return moji
    arr = []
    before = create(n - 1)
    for b in before:
        for m in moji:
            arr.append(b+m)

    return arr


ans = create(N)
for a in ans:
    print(a)
