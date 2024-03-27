# https://www.acmicpc.net/problem/11005
import sys

N, B = map(int, sys.stdin.readline().split())
result = 0

arr = []
while N:
    N, r = divmod(N, B)
    arr.append(r)

for i in arr[::-1]:
    if i > 9:
        print(chr(i + 55), end='')
    else:
        print(i, end='')