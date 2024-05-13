# https://www.acmicpc.net/problem/24313
import sys

a1, a0 = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

print(a1 * n + a0, '<=', c * n)

if a1 * n + a0 <= c * n and a1 <= c:
    print(1)
else:
    print(0)


