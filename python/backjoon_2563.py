# https://www.acmicpc.net/problem/2563
import sys

num = int(sys.stdin.readline().strip())
arr = [list(map(int,sys.stdin.readline().split())) for i in range(num)]

for i, val in enumerate(arr):
    x = val[0]
    y = val[1]

    print(x, x + 10)
