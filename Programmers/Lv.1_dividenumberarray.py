# 나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer = sorted(answer)
    
    return answer

arr = map(int, input().split())
divisor = int(input())

print(solution(arr, divisor))

# 다른 사람 풀이(if문 대신 or 사용하기)

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]