# https://www.acmicpc.net/problem/10798
import sys

arr = [list(map(str,sys.stdin.readline().split())) for i in range(5)]

for i in range(15):
    for j in range(5):
        if i >= len(arr[j][0]):
            continue
        print(arr[j][0][i], end='')
