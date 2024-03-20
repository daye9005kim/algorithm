# https://www.acmicpc.net/problem/2566
import sys

arr = [list(map(int,sys.stdin.readline().split())) for i in range(9)]

m = 0
idx = 0
idx2 = 0
for i, row in enumerate(arr):
    for j, val in enumerate(row):
        if m < val:
            m = val
            idx = i
            idx2 = j

print(m)
print(idx + 1, idx2 + 1)

