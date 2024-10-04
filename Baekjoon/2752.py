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

# 삽입 정렬 > 하향식(순환 구조)
A = list(map(int, input().split()))

def insertion_sort(li, n):
    if n == len(li): # 탈출 조건
        return li  # 정렬된 리스트를 반환
    else:
        key = li[n] # 이번에 삽입할 요소
        i = 0
        while i < n and li[i] < key: # key가 들어갈 위치를 찾기(for문 보다 while문이 효율적)
          i += 1
        li.insert(i, key)
        del li[n + 1]  # 마지막 요소 삭제 (중복 방지)
        
        return insertion_sort(li, n + 1)  # 재귀 호출

n = 1
sorted_list = insertion_sort(A, n)
print(*sorted_list)