# 2752번_세수정렬
# 동규는 세수를 하다가 정렬이 하고 싶어졌다.
# 정수 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어졌다.
# 정수 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

# 선택 정렬 > 제자리 정렬
li = list(map(int,input().split()))

for i in range(len(li)-1):
  for j in range(i+1, len(li)):
    if li[i] > li[j]:
      li[i], li[j] = li[j], li[i]

print(*li)