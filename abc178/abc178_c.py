N = int(input())
MOD = 10 ** 9 + 7
# 全パターンの数
subete = (10 ** N) % MOD
# 0を含まないパターン数
no_0 = (9**N) % MOD
# 9を含まないパターン数
no_9 = (9**N) % MOD
# 0も9も含まないパターン数
no_0_9 = (8**N) % MOD
ans = subete + no_0_9
ans -= no_0
# 引いた後に負の数だったら10**9+7を足す
if ans < 0:
    ans += MOD
ans -= no_9
# 引いた後に負の数だったら10**9+7を足す
if ans < 0:
    ans += MOD
print(ans)
