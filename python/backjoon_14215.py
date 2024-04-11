# https://www.acmicpc.net/problem/14215
import sys

t = sorted(list(map(int, sys.stdin.readline().split())))
if t[0] + t[1] <= t[2]:
    t[2] = t[0] + t[1] - 1
print(sum(t))
