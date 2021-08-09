# https://atcoder.jp/contests/abc175/tasks/abc175_b
N = int(input())
l_arr = list(map(int, input().split()))
l_arr.sort()
ans_set = set()
for i in range(N - 1):
    for j in range(i + 1, N):
        for k, l in enumerate(l_arr):
            if (l < l_arr[i] + l_arr[j] and l_arr[i] < l_arr[j] + l and l_arr[j] < l_arr[i] + l) and (l_arr[i] != l_arr[j] and l_arr[i] != l and l_arr[j] != l):
                ans_list = [i + 1, j + 1, k + 1]
                ans_list.sort()
                ans_set.add((ans_list[0], ans_list[1], ans_list[2]))
                continue
            if l >= l_arr[i] + l_arr[j]:
                break
print(len(ans_set))
