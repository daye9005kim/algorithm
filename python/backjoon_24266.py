# https://www.acmicpc.net/problem/24266
import sys

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

n = int(sys.stdin.readline().strip())
print(n ** 3)
print(3)
