 # https://www.acmicpc.net/problem/5622
import sys

a = sys.stdin.readline()

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in a:
    for index, string in enumerate(alphabet):
        if i in string:
            result += index + 3

print(result)
