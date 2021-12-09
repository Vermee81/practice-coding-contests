# https://atcoder.jp/contests/abc229/tasks/abc229_b
A, B = input().split()
revA = A[::-1]
revB = B[::-1]
min_len = min(len(A), len(B))

for i in range(min_len):
    if int(revA[i]) + int(revB[i]) > 9:
        print("Hard")
        exit()

print("Easy")
