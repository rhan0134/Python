# 2751번_수 정렬하기 2
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys

N = int(input())
li = [int(sys.stdin.readline()) for i in range(N)]

li.sort()

for i in li:
    print(i)