# 숫자 문자열과 영단어
'''
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.
0   zero
1   one
2   two
3   three
4   four
5   five
6   six
7   seven
8   eight
9   nine 
'''

def solution(s):
    answer = ''
    
    i = 0
    while(True):
        if i >= len(s):
            break
        
        if s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9':
            answer += s[i]
            i += 1
        else:
            if s[i] == 'z':
                answer += '0'
                i += 4
            elif s[i] == 'o':
                answer += '1'
                i += 3
            elif s[i] == 't':
                if s[i+1] == 'w':
                    answer += '2'
                    i += 3
                else:
                    answer += '3'
                    i += 5
            elif s[i] == 'f':
                if s[i+1] == 'i':
                    answer += '4'
                    i += 4
                else:
                    answer += '5'
                    i += 4
            elif s[i] == 's':
                if s[i+1] == 'i':
                    answer += '6'
                    i += 3
                else:
                    answer += '7'
                    i += 5
            elif s[i] == 'e':
                answer += '8'
                i += 5
            elif s[i] == 'n':
                answer += '9'
                i += 4
                    
                    
    return answer

s = input()

print(solution(s))


# 다른 사람 풀이1(딕셔너리 사용)
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value) #replace(찾을 값, 바꿀 값)
    return int(answer)

# 다른 사람 풀이2(리스트 사용)
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)