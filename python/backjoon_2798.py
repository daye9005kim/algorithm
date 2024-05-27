# https://www.acmicpc.net/problem/2798
import sys

n, m = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline().split()
arr = list(map(int, arr))
arr.sort()
print(arr)

h = len(arr)
tmp = 0
sum = 0
max = []
for i in range(h):
    for j in range(i + 1, h):
        for k in range(j + 1, h):
            sum = int(arr[i]) + int(arr[j]) + int(arr[k])

            if tmp < sum <= m:
                print(arr[i], '+', arr[j], '+', arr[k], '=', sum)
                max.append(sum)
                break

            tmp = sum


max.sort()
print(max[-1])