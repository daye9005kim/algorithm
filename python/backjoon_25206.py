# https://www.acmicpc.net/problem/25206
import sys

arr = [sys.stdin.readline().strip() for i in range(20)]
levels = {'A+':4.5, 'A0':4.0,  'B+':3.5,  'B0':3.0,  'C+':2.5,  'C0':2.0,  'D+':1.5,  'D0':1.0,  'F':0}

major_hap = 0
point_hap = 0
for sub in arr:
    title, point, level = sub.split()
    if level == 'P':
        continue

    major_hap += float(point) * levels[level]
    point_hap += float(point)

if point_hap > 0:
    print("{:.6f}".format(major_hap / point_hap))
else:
    print(0)

