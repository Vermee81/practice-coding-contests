# https://atcoder.jp/contests/abc157/tasks/abc157_c
N, M = map(int, input().split())
start = 10 ** (N - 1) if N != 1 else 0
end = start * 10 - 1 if N != 1 else 9

if M == 0:
    print(start)
    exit()
sc_set = set()
for _ in range(M):
    s, c = map(int, input().split())
    sc_set.add((s, c))

for i in range(start, end + 1):
    str_i = str(i)
    hantei = True
    for sc in sc_set:
        if int(str_i[sc[0] - 1]) != sc[1]:
            hantei = False
            break
    if hantei:
        print(i)
        exit()
print(-1)
