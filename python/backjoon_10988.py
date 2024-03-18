 # https://www.acmicpc.net/problem/10988
import sys

text = sys.stdin.readline().strip().upper()
key = list(set(text))
cnt = []
for i in key:
    cnt.append(text.count(i))

max_cnt = max(cnt)
if cnt.count(max_cnt) > 1:
    print("?")
else:
    print(key[cnt.index(max_cnt)])
