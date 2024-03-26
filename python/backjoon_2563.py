# https://www.acmicpc.net/problem/2563
import sys

num = int(sys.stdin.readline().strip())

tmp = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            tmp[i][j] = 1

result = 0
for li in tmp:
    result += sum(li)

print(result)