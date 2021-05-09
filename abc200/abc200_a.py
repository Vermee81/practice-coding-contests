N = int(input())
ans = 0
if N % 100 == 0:
    ans = N // 100
else:
    ans = (N // 100) + 1
print(ans)
