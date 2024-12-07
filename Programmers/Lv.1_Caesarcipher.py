# 시저 암호
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 내 풀이
def solution(s, n):
    answer = ''
    s = list(s)
    
    #A => 65 Z=> 90
    #a => 97 z => 122
    
    for i in s:
        if 65 <= ord(i) <= 90:
            if ord(i)+n > 90:
                answer += chr(64+(ord(i)+n)-90)
            else:
                answer += chr(ord(i)+n)
        elif 97 <= ord(i) <= 122:
            if ord(i)+n > 122:
                answer += chr(96+((ord(i)+n)-122))
            else:
                answer += chr(ord(i)+n)
        else:
            answer += " "
    
    return answer
    
s = input()
n = int(input())

print(solution(s, n))

# 다른 사람 풀이(아직 이해 부족)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper(): #65 <= ord(i) <= 90를 더 간단하게 표현하는 방법
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower(): #97 <= ord(i) <= 122를 더 간단하게 표현하는 방법
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)