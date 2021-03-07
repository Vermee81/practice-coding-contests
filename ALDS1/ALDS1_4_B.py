# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
N = int(input())
S = list(map(int, input().split()))
S.sort()
Q = int(input())
T = list(map(int, input().split()))
count = 0
for t in T:
    high = N - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if S[mid] == t:
            count += 1
            break
        if S[mid] > t:
            high = mid - 1
            continue
        low = mid + 1
print(count)
