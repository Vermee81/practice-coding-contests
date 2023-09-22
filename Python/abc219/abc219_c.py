# https://atcoder.jp/contests/abc219/tasks/abc219_c
X = input()
x_dict = {}
for i, x in enumerate(X):
    x_dict[x] = i + 1
N = int(input())
s_arr = []
for _ in range(N):
    s_arr.append(input())


def l_is_smaller(left: str, right: str):
    min_len = min(len(left), len(right))
    for i in range(min_len):
        if left[i] != right[i]:
            if x_dict[left[i]] < x_dict[right[i]]:
                return True
            return False
    if len(left) < len(right):
        return True
    return False


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if l_is_smaller(left[l_i], right[r_i]) or left[l_i] == right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


ans = merge_sort(s_arr)
for a in ans:
    print(a)
