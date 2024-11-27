# 두 정수 사이의 합
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 내 풀이
def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer += i
    elif a == b:
        answer = a
    else:
        for i in range(b, a+1):
            answer += i
    
    return answer

a, b = map(int, input().split())

print(solution(a,b))


# 다른 사람 풀이 1(등차수열의 합)
# 첫째항: a, 공차: d, 제 n항이 l인 등차수열의 합 => S_n = n(a+l)/2
# 이 경우 a = a or b, 공차 = 1, n항 = a or b
# n => abs(a-b)+1
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 다른 사람 풀이 2
def adder(a, b):
    if a > b: #if문을 활용해서 순서를 바꾸기
        a, b = b, a 
    return sum(range(a, b + 1))