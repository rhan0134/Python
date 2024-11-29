# 정수 제곱근 판별

# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

#내 풀이(while문과 if문 사용)
def solution(n):
    answer = 0
    
    i = 1
    
    while answer < n:
        
        answer = i*i
        
        i += 1
    
    if answer == n:
        answer = i*i
    else:
        answer = -1
    
    return answer

n = int(input())

print(solution(n))

# 다른 사람 풀이
def nextSqure(n):
    sqrt = n ** (1/2) #1/2를 제곱해 제곱근 찾기

    if sqrt % 1 == 0: #만약 1로 나눴을 때 나머지가 0이면
        return (sqrt + 1) ** 2
    
    return -1