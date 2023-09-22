# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
N = int(input())
ab_arr = []
minimum = 1 << 64 - 1
for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_arr.append((a, b))
for i in range(N):
    for j in range(N):
        iri = ab_arr[i][0]
        degu = ab_arr[j][1]
        amount = 0
        for ab in ab_arr:
            amount += abs(iri - ab[0]) + abs(ab[0] - ab[1]) + abs(ab[1] - degu)
        minimum = min(amount, minimum)
print(minimum)
