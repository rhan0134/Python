# 문자열 내 p와 y의 개수
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 내 풀이(if문 사용)
def solution(s):
    answer = True
    countp, county = 0, 0
    
    for i in s:
        if i == 'p' or i == 'P':
            countp+= 1
        elif i == 'y' or i == 'Y':
            county+= 1

    if countp!=county:
        answer = False

    return answer

s = input()

print(solution(s))

# 다른 사람 풀이(if문 사용 X)
def numPY(s):
    # lower()로 다 소문자로 만든 다음에 count()
    return s.lower().count('p') == s.lower().count('y')