# 평균 구하기
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def solution(arr):
    answer = 0
    
    answer = sum(arr)/len(arr) #평균
    
    return answer

arr = list(map(int, input().split()))

print(solution(arr))