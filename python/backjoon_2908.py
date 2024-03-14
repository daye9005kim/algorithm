 # https://www.acmicpc.net/problem/2908
import sys

a, b = map(str, sys.stdin.readline().split())

a = int(a[::-1])
b = int(b[::-1])

print(max(a,b))


