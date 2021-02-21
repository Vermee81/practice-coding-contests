def z_algorithm(moji: str) -> list:
    n = len(moji)
    ans = [0 for _ in range(n)]
    ans[0] = n
    left, right = 1, 1
    for i in range(1, n):
        ans[i] = min(ans[i - left], right - i)
        ans[i] = max(0, ans[i])
        while i + ans[i] < n and moji[i + ans[i]] == moji[ans[i]]:
            ans[i] += 1
        if right < ans[i] + i:
            right = ans[i] + i
            left = i
    return ans


if __name__ == '__main__':
    s = input()
    ans_arr = z_algorithm(s)
    answer = " ".join([str(i) for i in ans_arr])
    print(answer)
