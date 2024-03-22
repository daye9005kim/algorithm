# https://www.acmicpc.net/problem/2745
import sys

N, B = map(str, sys.stdin.readline().split())
N = N.upper()
B = int(B)
result = 0

for idx, val in enumerate(N):
    s = len(N) - 1 - idx
    asc = ord(val)
    m = int(val) if 47 < asc < 58 else asc - 55
    result += (B ** s) * m

print(result)


