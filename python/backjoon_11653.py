# https://www.acmicpc.net/problem/11653
import sys

a = int(sys.stdin.readline().strip())
result = []

if a < 2:
    sys.exit()

# 제곱근
for i in range(2, int(a ** (1 / 2)) + 1):
    while a % i < 1:
        a = a // i
        print(i)
if a > 1:
    print(a)