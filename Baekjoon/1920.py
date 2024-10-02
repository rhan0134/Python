# 1920번_수 찾기
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

#1) 순환 구조
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이진 탐색을 위해 먼저 정렬된 리스트 만들기
A = sorted(A)

def binary_search(A, key, low, high): #low:탐색해야 하는 항목의 가장 작은 인덱스 , high: 탐색해야 하는 항목의 가장 큰 인덱스
    if low <= high: #탐색해야 하는 항목이 남아 있으면(종료 조건)
        mid = (low + high) // 2 # 중간값 인덱스
        if key == A[mid]: # 탐색 성공하면 1을 반환한다
            return 1
        elif key < A[mid]: # 중앙의 항목보다 찾는 값이 작다면 중앙 항목의 왼쪽을 탐색
            return binary_search(A, key, low, mid-1)
        else: # 중앙의 항목보다 찾는 값이 크다면 중앙 항목의 오른쪽을 탐색
            return binary_search(A, key, mid+1, high)
    return 0 # 탐색 실패 시 0 반환 

low = 0
high = N-1
for key in B:
    print(binary_search(A, key, low, high))


#2) 반복 구조
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이진 탐색을 위해 먼저 정렬된 리스트 만들기
A = sorted(A) #or A.sort()

def binary_search(A, key, low, high):
  while(low <= high): #탐색해야 하는 항목이 남아 있으면(종료 조건)
    mid = (low + high) // 2 # 중간값 인덱스
    if key == A[mid]: # 탐색 성공하면 1을 반환한다
            return 1
    elif key < A[mid]: # 중앙의 항목보다 찾는 값이 작다면 중앙 항목의 왼쪽을 탐색
        high = mid - 1
    else: # 중앙의 항목보다 찾는 값이 크다면 중앙 항목의 오른쪽을 탐색
        low = mid + 1
  return 0 # 탐색 실패 시 0 반환

low = 0
high = N-1
for key in B:
    print(binary_search(A, key, low, high))