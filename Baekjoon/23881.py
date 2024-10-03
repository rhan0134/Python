# 23881번_알고리즘 수업 - 선택 정렬 1
# 오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.
# 크기가 N인 배열에 대한 선택 정렬 의사 코드는 다음과 같다.
'''
selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}
'''

N, K = map(int, input().split()) #배열 A의 크기 N, 교환 횟수 K
A = list(map(int,input().split()))

def selection_sort(A):
    count = 0
    result = []
    for last in range(N-1,0,-1):
        inx = 0 # 첫 번째 요소를 가장 큰 값으로 가정
        for i in range(1,last+1): #last 이후 숫자는 이미 큰 수로 정렬이 완료
            if A[inx] < A[i]: 
              inx = i # 가장 큰 값 업데이트
        if last != inx: # 가장 큰 값이 last면 교환 X
          A[last], A[inx] = A[inx], A[last] #교환
          count += 1 #교환 횟수 증가
          if count == K:
            result.append(A[inx])
            result.append(A[last])
    if count < K:
        result.append(-1)
    return result

print(*selection_sort(A))