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
    if n <= 1: # 탈출 조건(배열의 크기가 1이면 정렬된 것으로 간주)
        return li  # 정렬된 리스트를 반환

    # 재귀 호출하여 앞의 n-1개를 정렬
    insertion_sort(li, n - 1)
    key = li[n-1] # 이번에 정렬해야 하는 요소
    i = n-2

    #key보다 큰 요소들을 오른쪽으로 이동
    while i >= 0 and li[i] > key:
      li[i+1] = li[i]
      i -= 1

    # key 삽입  
    li[i+1] = key
    return li

sorted_list = insertion_sort(A, len(A))
print(*sorted_list)

# 삽입정렬 > 상향식(왼쪽 항목부터 차례로 비교)
A = list(map(int, input().split()))

def insertion_sort(li):
  for i in range(1, len(li)):
    key = li[i] #이번에 삽입할 요소
    j = 0
  
    while j < i and li[j] < key: # key가 들어갈 위치를 찾기(for문 보다 while문이 효율적)
      j += 1
    li.insert(j, key)
    del li[i + 1]  # 요소 삭제 (중복 방지)
        
  return li  # 정렬된 리스트 반환

sorted_list = insertion_sort(A)
print(*sorted_list)