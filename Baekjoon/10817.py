# 10817번_세 수
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

# 선택 정렬 > 제자리 정렬
li = list(map(int,input().split()))

for i in range(len(li)-1):
  for j in range(i+1, len(li)):
    if li[i] > li[j]:
      li[i], li[j] = li[j], li[i]

print(li[1])