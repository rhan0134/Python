# 내적
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

#내 풀이 1(numpy)
import numpy as np

def solution(a, b):
    return np.dot(a,b)

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solution(a,b))

#내 풀이 2(for문)
def solution(a,b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i]*b[i]
    
    return answer

# 다른 사람 풀이(zip을 사용)
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])