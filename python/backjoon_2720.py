# https://www.acmicpc.net/problem/2720
import sys

n = int(sys.stdin.readline().strip())
coins = [25, 10, 5, 1]

for _ in range(n):
    m = int(sys.stdin.readline().strip())
    count = []

    for coin in coins:
        if m < coin:
            cnt = 0
        else:
            cnt, rest = divmod(m, coin)
            m = rest

        count.append(cnt)
    print(*count)

