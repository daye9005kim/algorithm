# https://www.acmicpc.net/problem/2581
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
result = []
for a in range(n, m + 1):
    if a < 2:
        continue

    # 제곱근
    for i in range(2, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            break
    else:
        result.append(a)

if len(result) < 1:
    print(-1)
    sys.exit()

print(sum(result))
print(result[0])
