# https://www.acmicpc.net/problem/24265
import sys

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

n = int(sys.stdin.readline().strip())
print(n * (n - 1) // 2)
print(2)
