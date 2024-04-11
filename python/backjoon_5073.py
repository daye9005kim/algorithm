# https://www.acmicpc.net/problem/5073
import sys

while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    t = sorted([a, b, c])
    a = t[0]
    b = t[1]
    c = t[2]

    if a == b == c:
        print("Equilateral")
    elif a + b <= c or 0 in t:
        print("Invalid")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
