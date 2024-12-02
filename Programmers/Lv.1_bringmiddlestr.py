# 가운데 글자 가져오기
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 내 풀이(if-else문)
def solution(s):
    answer = 0
    
    if len(s)%2==0:
        answer = s[len(s)//2-1:len(s)//2+1]
    else:
        answer = s[len(s)//2]
    
    return answer
    
s = input()
print(solution(s))

# 다른 사람 풀이(문제에 맞는 수식)
def string_middle(str):
    # 1)abcde => str[2:3]
    # 2)qwer => str[1:3]
    return str[(len(str)-1)//2 : len(str)//2 + 1]