# https://www.acmicpc.net/problem/9506
import sys

while 1:
    a = int(sys.stdin.readline().strip())
    if a < 0:
        sys.exit()

    i = 0
    arr = []

    # 제곱근
    r = a ** (1 / 2)
    if r - int(r) > 0:
        r += 1

    while i < int(r):
        i += 1
        if a % i > 0:
            continue
        arr.append(i)
        if int(a / i) == a:
            continue
        arr.append(int(a / i))

    arr = sorted(set(arr))
    if sum(arr) == a:
        print(sum(arr), '=', ' + '.join(map(str, arr)))
    else:
        print(a, 'is NOT perfect.')
