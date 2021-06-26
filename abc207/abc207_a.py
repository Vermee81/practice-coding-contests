# https://atcoder.jp/contests/abc207/tasks/abc207_a
three_nums = list(map(int, input().split()))
three_nums.sort(reverse=True)
print(three_nums[0] + three_nums[1])
