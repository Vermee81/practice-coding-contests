# https://atcoder.jp/contests/abc210/tasks/abc210_b
N = int(input())
S = input()
for i in range(N):
    if S[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
            exit()
        else:
            print('Aoki')
            exit()
