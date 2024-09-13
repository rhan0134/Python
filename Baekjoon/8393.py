# 8393번_합
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

#1
num = int(input())
sum = 0

for n in range(num):#0,1,2
  sum += n+1

print(sum)

#2
num = int(input())
sum = 0

for n in range(1,num+1):
    sum += n

print(sum)