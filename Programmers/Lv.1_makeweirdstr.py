# 이상한 문자 만들기
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 내 풀이 1
def solution(s):
    li = list(s.split(' '))
    result = []
    
    for i in li:
        answer = ''
        for j in range(len(i)):
            if j%2==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        
        result.append(answer)
       
    return " ".join(result)

s = input()

print(solution(s))

# 내 풀이 2 (for문 방식이 조금 다름)
def solution(s):
    s = s.split(" ") #다른 사람 풀이에서 참고
    
    for i in range(len(s)):
        answer = ''
        for j in range(len(s[i])):
            if j%2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        
        s[i] = answer
    
    return " ".join(s)