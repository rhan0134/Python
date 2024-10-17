# 10818번_최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
N_li = list(map(int, input().split()))
print(min(N_li), max(N_li))