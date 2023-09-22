# https://atcoder.jp/contests/abc194/tasks/abc194_b
N = int(input())
job_list = []
a_min_idx, b_min_idx = 0, 0
a_2nd, b_2nd = 0, 0
for i in range(N):
    a, b = list(map(int, input().split()))
    job_list.append([a, b])
    if job_list[a_min_idx][0] > a:
        a_2nd = a_min_idx
        a_min_idx = i
    if job_list[b_min_idx][1] > b:
        b_2nd = b_min_idx
        b_min_idx = i
ans = 0
if a_min_idx == b_min_idx:
    ans = min(max(job_list[a_min_idx][0], job_list[b_2nd][1]), max(job_list[a_2nd][0], job_list[b_min_idx][1]),
              job_list[a_min_idx][0] + job_list[b_min_idx][1])
    print(ans)
    exit()
ans = max(job_list[a_min_idx][0], job_list[b_min_idx][1])
print(ans)


