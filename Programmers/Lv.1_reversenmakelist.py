# 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 내 풀이(for문 사용하기)
def solution(n):
    answer = []
    
    for i in str(n)[::-1]:
        answer.append(int(i))
    
    return answer

n = int(input())

print(solution(n))

# 다른 사람 풀이(map 사용하기)
def digit_reverse(n):
    return list(map(int, reversed(str(n))))