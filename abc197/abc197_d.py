# https://atcoder.jp/contests/abc197/tasks/abc197_d
from math import pi, cos, sin
N = int(input())
x0, y0 = map(int, input().split())
x_N_2, y_N_2 = map(int, input().split())
x_mid = (x0 + x_N_2) / 2
y_mid = (y0 + y_N_2) / 2

deg = (2*pi/N) - pi

cos_deg = cos(deg)
sin_deg = sin(deg)

ans_x = cos_deg * (x_N_2 - x_mid) - sin_deg * (y_N_2 - y_mid) + x_mid
ans_y = sin_deg * (x_N_2 - x_mid) + cos_deg * (y_N_2 - y_mid) + y_mid

print(ans_x, ans_y)
