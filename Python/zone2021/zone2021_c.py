# https://atcoder.jp/contests/zone2021/tasks/zone2021_c
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]


def check(x):
    s = set()
    for a in A:
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    for member1 in s:
        for member2 in s:
            for member3 in s:
                if member1 | member2 | member3 == 31:
                    return True
    return False


ok = 0
ng = 10**9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
