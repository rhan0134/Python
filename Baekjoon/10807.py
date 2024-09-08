# 10807번_개수 세기
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.


#1
sum = 0
N = int(input())
N_li = list(map(int, input().split()))
v = int(input())

for n_li in N_li:
    if n_li == v:
        sum+= 1

print(sum)

#2
N = int(input())
N_li = list(map(int, input().split()))
v = int(input())

print(N_li.count(v))