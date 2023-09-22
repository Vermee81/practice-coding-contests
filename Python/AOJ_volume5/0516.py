# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0516
def solve(n: int, k: int, a_arr: list) -> int:
    acc = [0 for _ in range(n)]
    acc[0] = a_arr[0]
    for i in range(1, n):
        acc[i] = acc[i - 1] + a_arr[i]

    j = 0
    ans = 0
    while j + k < n:
        ans = max(ans, acc[j + k] - acc[j])
        j += 1
    return ans


while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        exit()
    a_arr = [int(input()) for _ in range(n)]
    print(solve(n, k, a_arr))


