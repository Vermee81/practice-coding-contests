# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
N = int(input())
A_arr = list(map(int, input().split()))
Q = int(input())
Q_arr = list(map(int, input().split()))
dp = []


def rec(i: int, w: int) -> int:
    if dp[i][w] != -1: return dp[i][w]
    if i == 0:
        if w == 0:
            return 1
        else:
            return 0
    ans = 0
    if w >= A_arr[i - 1] and rec(i - 1, w - A_arr[i - 1]) == 1: ans = 1
    if rec(i - 1, w) == 1: ans = 1
    dp[i][w] = ans
    return ans


for q in Q_arr:
    dp = [[-1 for _ in range(q+1)] for _ in range(N+1)]
    # i個の数を選んだ時に合計がwになるときは1ならないときは0、初期値は-1
    # dp[i][w] = dp[i-1][w]
    # dp[i][w] = dp[i-1][w - A_arr[i-1]] + A_arr[i-1]
    answer = 'no'
    if rec(N, q) == 1:
        answer = 'yes'
    print(answer)
