# 문자열 내 마음대로 정렬하기
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    #x[n]을 기준으로 정렬, 만약 같으면 사전 순으로 정렬
    #lambda 함수 => lambda 매개변수 : 표현식
    return sorted(strings, key=lambda x : (x[n], x))

strings = list(map(str,input().split()))
n = int(input())

print(solution(strings, n))