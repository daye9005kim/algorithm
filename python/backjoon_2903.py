# https://www.acmicpc.net/problem/2903
import sys

n = int(sys.stdin.readline().strip())
m = 2
for _ in range(n):
    m = m * 2 - 1

print(m * m)

