 # https://www.acmicpc.net/problem/3003
import sys

arr = sys.stdin.readline().split()
chess = [1, 1, 2, 2, 2, 8]
for index, string in enumerate(arr):
    n = chess[index] - int(string)
    print(n)