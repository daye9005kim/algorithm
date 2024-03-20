# https://www.acmicpc.net/problem/2738
import sys

x, y = map(int,sys.stdin.readline().split())

A = []
for i in range(x * 2):
    A.append(list(map(int,sys.stdin.readline().split())))

h = []
for i in range(x):
    tmp = [int(A[i][j]) + int(A[i + x][j]) for j in range(y)]
    print(*tmp)