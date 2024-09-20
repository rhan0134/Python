# 2750번_수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input())
li = []

for i in range(N):
    a = int(input())
    li.append(a)

for i in range(len(li)-1):
  for j in range(i+1, len(li)):
    if li[i] > li[j]:
      li[i], li[j] = li[j], li[i]

for i in range(N):
    print(li[i])