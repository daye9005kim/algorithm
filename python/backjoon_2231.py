# https://www.acmicpc.net/problem/2231
import sys

n = int(sys.stdin.readline().strip())
m = 0

for i in range(1, n + 1):
    s = sum(map(int, str(i)))
    if i + s == int(n):
        m = i
        break
print(m)
