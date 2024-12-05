# 최대공약수와 최소공배수
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 내 풀이
def solution(n, m):
    answer = []
    result = []
    
    #n의 공약수 구하기(만약 n이 더 큰 수라면 약간의 낭비)
    # 밑의 크기 비교를 적용하면 낭비를 줄일 수 있을 것 같음
    # c = min(a,b) -> for i in range(1,c+1): if c%i == 0: ...
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)
            
    for i in result[-1::-1]:# n의 공약수를 모아놓은 리스트를 거꾸로 실행하면서 최대공약수 찾기
        if m%i == 0: 
            answer.append(i)# m과의 최대공약수
            answer.append(i*(n//i)*(m//i))# 최대공배수를 구하는 방법
            break

    return answer
        
n, m = map(int, input().split())

print(solution(n, m))
          

# 다른 사람 풀이(유클리드 호제법) or gcd() 사용하기
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b) #크기 비교
    t = 1
    while t>0:
        t = c%d 
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer