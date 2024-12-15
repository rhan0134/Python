# 2016년
# 2016년 1월 1일은 금요일입니다. 
# 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다. 
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

def solution(a, b):
    d = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU", ]
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #m[:a-1]: 전 달까지 날짜 다 더하기 / (b-1): 해당달 일 더하기 / %7: 요일 찾기
    return d[(sum(m[:a-1])+(b-1))%7] 
    
a = int(input())
b = int(input())

print(solution(a,b))