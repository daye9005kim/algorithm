# https://www.acmicpc.net/problem/3009
import sys

tmp_x = []
tmp_y = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x not in tmp_x:
        tmp_x.append(x)
    else:
        tmp_x.remove(x)
    if y not in tmp_y:
        tmp_y.append(y)
    else:
        tmp_y.remove(y)

print(*tmp_x, *tmp_y)
