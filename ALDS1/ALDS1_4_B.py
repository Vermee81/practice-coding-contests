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
    while low + 1 < high:
        mid = (high + low) // 2
        if S[mid] == t or S[high] == t or S[low] == t:
            count += 1
            break
        elif S[mid] > t:
            high = mid
        else:
            low = mid
print(count)
