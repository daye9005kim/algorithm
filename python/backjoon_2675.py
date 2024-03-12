 # https://www.acmicpc.net/problem/2675
 # 문자열 반복

import sys

times = int(sys.stdin.readline())
arr = []
for _ in range(times):
    R, STRING = map(str, sys.stdin.readline().split())
    result = ''
    for S in STRING:
        result += S * int(R)
    print(result)
