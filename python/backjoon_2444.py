 # https://www.acmicpc.net/problem/2444
import sys

a = int(sys.stdin.readline())
stars = []

for i in range(1, a + 1):
    n = i * 2 - 1
    m = a - i
    stars.append(" " * m + "*" * n)

result = stars + stars[-2::-1]

print('\n'.join(map(str, result)))

