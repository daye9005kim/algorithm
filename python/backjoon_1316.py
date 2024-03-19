# https://www.acmicpc.net/problem/1316
import sys

num = int(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip() for i in range(num)]
result = 0

for text in arr:
    key = len(list(set(text)))
    chng = 0
    length = len(text)

    for i in range(length):
        if length > i + 1 and text[i] != text[i + 1]:
            chng += 1

    if key > chng or chng == 0:
        result += 1

print(result)
