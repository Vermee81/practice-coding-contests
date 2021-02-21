
if __name__ == '__main__':
    
    N = int(input())
    xy_arr = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    op_arr = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    ab_arr = [list(map(int, input().split())) for _ in range(Q)]
    ans_arr = [xy_arr]


    def rot_plus_90(xy):
        return [xy[1], -xy[0]]


    def rot_minus_90(xy):
        return [-xy[1], xy[0]]


    def taisho_x(x, xy):
        return xy if xy[0] == x else [2 * x - xy[0], xy[1]]


    def taisho_y(y, xy):
        return xy if xy[1] == y else [xy[0], 2 * y - xy[1]]


    for op in op_arr:
        if len(op) == 2 and op[0] == 3:
            nxy = []
            for xy in ans_arr[-1]:
                nxy.append(taisho_x(op[1], xy))
            ans_arr.append(nxy)
            continue
        if len(op) == 2 and op[0] == 4:
            nxy = []
            for xy in ans_arr[-1]:
                nxy.append(taisho_y(op[1], xy))
            ans_arr.append(nxy)
            continue
        if op[0] == 1:
            nxy = []
            for xy in ans_arr[-1]:
                nxy.append(rot_plus_90(xy))
            ans_arr.append(nxy)
            continue
        if op[0] == 2:
            nxy = []
            for xy in ans_arr[-1]:
                nxy.append(rot_minus_90(xy))
            ans_arr.append(nxy)
            continue

    for ab in ab_arr:
        ans = ans_arr[ab[0]][ab[1] - 1]
        print(f"{ans[0]} {ans[1]}")
