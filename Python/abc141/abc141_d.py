# https://atcoder.jp/contests/abc141/tasks/abc141_d
from heapq import heapify, heappop, heappush
N, M = map(int, input().split())
a_arr = list(map(lambda x: int(x) * -1, input().split()))
heapify(a_arr)

for i in range(M):
    most_expensive = heappop(a_arr)
    most_expensive = ((-1 * most_expensive) // 2) * -1
    heappush(a_arr, most_expensive)

print(-1 * sum(a_arr))
