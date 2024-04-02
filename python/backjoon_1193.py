# https://www.acmicpc.net/problem/1193
import sys

n = int(sys.stdin.readline().strip())
sum = 0
dd = 0
line = 1

for i in range(1, n + 1):
    sum += i
    dd = sum - n

    if dd >= 0:
        line = i
        break

if line % 2 < 1:
    a = line - dd
    b = 1 + dd
else:
    a = 1 + dd
    b = line - dd

print(f'{a}/{b}')
