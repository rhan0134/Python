# 3진법 뒤집기
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = ''
    while n>=1: #or while n:
        answer += str(n%3) # 10진법 => 3진법
        n = n//3
    
    #answer = answer[-1::-1] => 이게 원래 3진법

    return int(answer,3) #3진법 => 10진법

n = int(input())

print(solution(n))