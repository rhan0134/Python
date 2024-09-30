# 24051번_알고리즘 수업 - 삽입 정렬 1
# 오늘도 서준이는 삽입 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 삽입 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.
# 크기가 N인 배열에 대한 삽입 정렬 의사 코드는 다음과 같다.
'''
insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for i <- 2 to N {
        loc = i - 1;
        newItem = A[i];

        # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (1 <= loc and newItem < A[loc]) {
            A[loc + 1] <- A[loc];
            loc--;
        }
        if (loc + 1 != i) then A[loc + 1] = newItem;
    }
}
'''

N, K = map(int, input().split()) # A: 배열 A의 크기, K: 저장 횟수
A = list(map(int, input().split())) # 배열 A의 원소 입력

def insertion_sort(A): # A[0...N-1]를 오름차순으로 정렬
    count = 0 # 저장 횟수
    result = 0 # K번째 저장되는 수

    for i in range(1,N): # 왼쪽 숫자부터 정렬하기 때문에 (A[0],A[1]을 먼저 정렬)
        loc = i - 1 # 0~i-1번째는 정렬된 부분 / i부터 끝까지는 아직 정렬이 되지 않은 부분
        newItem = A[i] #마지막에 복사할 숫자 저장(이번에 정렬하는 숫자 A[i])
    
        # 정렬된 항목에 정렬 안 된 항목 하나를 비교해서 끼워넣는 과정
        # A[1] ~ A[i-1]은 이미 정렬된 상태
        while 0 <= loc and newItem < A[loc]: #비교항목이 A[i]보다 큰 경우
            A[loc+1] = A[loc] # 앞의 항목들을 뒤로 복사
            loc -= 1
            count += 1

            if count == K:
              result = A[loc+1]
              
        
        if loc + 1 != i: # Sorting이 이미 되어있을 경우 skip => 없어도 되는 코드
          A[loc+1] = newItem # A[i]
          count += 1
          if count == K:
              result = newItem
    
    if K > count:
      result = -1
        
    return result

print(insertion_sort(A))