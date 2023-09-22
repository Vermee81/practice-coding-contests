# https://atcoder.jp/contests/abc116/tasks/abc116_c
N = int(input())
h_arr = list(map(int, input().split()))
ans = 0
h_sum = sum(h_arr)
while h_sum != 0:
    is_continue = False
    for i in range(N):
        if h_arr[i] != 0:
            if not is_continue:
                ans += 1
                is_continue = True
            h_arr[i] -= 1
        else:
            if is_continue:
                is_continue = False
    h_sum = sum(h_arr)

print(ans)
