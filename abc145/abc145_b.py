# https://atcoder.jp/contests/abc145/tasks/abc145_b
N = int(input())
S = input()

if len(S) % 2 == 1:
    print('No')
    exit()

for i in range(len(S) // 2):
    if S[i] != S[i + (len(S) // 2)]:
        print('No')
        exit()
print('Yes')
