# https://www.acmicpc.net/problem/9506
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for a in arr:
    if a < 2:
        continue
    # 제곱근
    for i in range(2, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            break
    else:
        result += 1
print(result)
