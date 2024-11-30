# 음양 더하기
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

def solution(absolutes, signs):
    
    for i,j in zip(absolutes, signs):
        if j == False:
            absolutes[absolutes.index(i)] = -i
    
    return sum(absolutes)

absolutes = list(map(int, input().split()))
signs = list(map(str, input().split()))

print(solution(absolutes, signs))