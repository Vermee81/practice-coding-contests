# https://atcoder.jp/contests/abc087/tasks/arc090_a
N = int(input())
a_arr = list()
a_arr.append(list(map(int, input().split())))
a_arr.append(list(map(int, input().split())))

first_rui = [0] * N
for i in range(N):
    before = first_rui[i - 1] if i > 0 else 0
    first_rui[i] = before + a_arr[0][i]

second_back_rui = [0] * N
for i in range(N - 1, -1, -1):
    forward = second_back_rui[i + 1] if i < N - 1 else 0
    second_back_rui[i] = forward + a_arr[1][i]

ans = 0
for i in range(N):
    ans = max(first_rui[i] + second_back_rui[i], ans)

print(ans)
