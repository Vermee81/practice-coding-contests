N = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
min_v, max_v = -1, 10000
for i in range(0, N):
    # a_arr[i] <= x <= b_arr[i]
    min_v = max(min_v, a_arr[i])
    max_v = min(max_v, b_arr[i])
    if min_v > max_v:
        print(0)
        exit()
print(max_v - min_v + 1)
