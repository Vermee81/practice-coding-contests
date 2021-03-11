# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
N = int(input())
xl_list = []
for _ in range(N):
    xi, li = list(map(int, input().split()))
    xl_list.append([xi - li, xi + li])

sorted_xl = sorted(xl_list, key=lambda x: x[1])
upper = -10 ** 9 - 1
ans = 0
for xl in sorted_xl:
    # かぶっていたら次のループ
    if upper > xl[0]:
        continue
    ans += 1
    upper = max(upper, xl[1])

print(ans)
