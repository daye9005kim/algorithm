# https://www.acmicpc.net/problem/2869
import sys

a, b, v = map(int, sys.stdin.readline().split())

x = (v - a) // (a - b)
if (v - a) % (a - b) > 0:
    x += 1

print(x + 1)
