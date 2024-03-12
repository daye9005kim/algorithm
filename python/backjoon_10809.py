 # https://www.acmicpc.net/problem/10809
 # 알파벳 찾기

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
name = sys.stdin.readline()

for i in alphabet:
    if i in name:
        print(name.index(i))
    else:
        print(-1)

