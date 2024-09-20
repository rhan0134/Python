# 10818번_최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.


#1 => 시간: 372ms
N = int(input())
N_li = list(map(int, input().split()))
print(min(N_li), max(N_li))

#2 선택 정렬 > 제자리 정렬 => 시간: 시간 초과
N = int(input())
li = list(map(int,input().split()))

for i in range(len(li)-1):
  for j in range(i+1, len(li)):
    if li[i] > li[j]:
      li[i], li[j] = li[j], li[i]

print(li[0], li[N-1])