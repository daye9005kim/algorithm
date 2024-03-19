# https://www.acmicpc.net/problem/10988
# 두번째 풀이
import sys

x = sys.stdin.readline().strip().upper()
arr = [0 for _ in range(91 - 65)]

for i in range(65, 91):
    c = chr(i)
    count = x.count(c)
    arr[i - 65] = count

M = max(arr)
if arr.count(M) > 1:
    print('?')
else:
    print(chr(arr.index(M) + 65))
