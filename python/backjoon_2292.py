# https://www.acmicpc.net/problem/2292
import sys

while 1:
    n = int(sys.stdin.readline().strip())
    m = 1
    i = 1
    while m < n:
        m += 6 * i
        i += 1

    print(i)