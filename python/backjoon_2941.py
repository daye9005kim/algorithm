# https://www.acmicpc.net/problem/2941
import sys

x = sys.stdin.readline().strip().lower()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for s in arr:
    x = x.replace(s, '0')

print(len(x))