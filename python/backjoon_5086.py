# https://www.acmicpc.net/problem/5086
import sys

arr = []
while 1:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break
    elif a % b < 1:
        arr.append('multiple')
    elif b % a < 1:
        arr.append('factor')
    else:
        arr.append('neither')

print(* arr)