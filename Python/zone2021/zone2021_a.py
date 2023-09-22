S = input()
L = 'ZONe'
ans = 0
for i in range(len(S) - 3):
    if S[i] == L[0] and S[i + 1] == L[1] and S[i + 2] == L[2] and S[i + 3] == L[3]:
        ans += 1
print(ans)
