# https://www.acmicpc.net/problem/2798
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.reverse()

sum = 0
max = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if arr[i] + arr[j] >= m:
            continue
        for k in range(j + 1, n):
            sum = arr[i] + arr[j] + arr[k]
            if max <= sum <= m: max = sum
print(max)
