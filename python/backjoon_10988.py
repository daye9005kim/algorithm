 # https://www.acmicpc.net/problem/10988
import sys

a = sys.stdin.readline().strip()

if a == a[::-1]:
    print(1)
else:
    print(0)

