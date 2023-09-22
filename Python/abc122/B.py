N, M = list(map(int, input().split()))
a_list = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    a_list[i] = list(map(int, input().split()))
ans = 0
for t1 in range(M-1):
    for t2 in range(t1+1, M):
        score = 0
        for i in range(N):
            score += max(a_list[i][t1], a_list[i][t2])
        ans = max(ans, score)
print(ans)

