# https://www.acmicpc.net/problem/2501
import sys

a, b = map(int, sys.stdin.readline().split())
arr = []
c = 0
for i in range(1, a + 1):
    if a % i < 1:
        arr.append(i)
        c += 1

    if c == b:
        break

if c < b:
    print(0)
else:
    print(arr[c - 1])
