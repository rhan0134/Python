# 문자열 다루기 기본
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

#내 풀이(48 ~ 57)
def solution(s):
    answer = 0
    
    if len(s) == 4:
        for i in s:
            if 48 <= ord(i) <=57:
                answer += 1
        
        if answer == 4:
            return True
        else:
            return False
    
    elif len(s) == 6:
        for i in s:
            if 48 <= ord(i) <=57:
                answer += 1
        
        if answer == 6:
            return True
        else:
            return False
    
    else:
        return False      
                
    

s = input()

print(solution(s))


# 다른 사람 풀이(isdigit => 문자열이 십진수로 변경이 가능하면 true, 아니면 false를 반환하는 함수)
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]