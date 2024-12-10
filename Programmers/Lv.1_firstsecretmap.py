# [1차] 비밀지도
'''
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.
'''

# 내 풀이
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        #2진수 구하기
        two1 = ''
        two2 = ''
        
        while arr1[i]/2 >= 0.5:
            two1 += str(arr1[i]%2)
            arr1[i] //= 2
        
        while arr2[i]/2 >= 0.5:
            two2 += str(arr2[i]%2)
            arr2[i] //= 2
        
        two1 = (n-len(two1))*'0' + two1[::-1]
        two2 = (n-len(two2))*'0' + two2[::-1]
        result = ''
        
        for i in range(len(two1)):
            if two1[i] == '1' or two2[i] == '1':
                result += '#'
            else:
                result += ' '
        
        answer.append(result)
        
    return answer

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(solution(n, arr1, arr2))


# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        #(i|j) => or 먼저 적용 후 이진변환(bin())
        # 모두 0이 나오면 0, 아니면 1로 바꿈
        a12 = str(bin(i|j)[2:]) #[2:] => 0b 없애기
        a12=a12.rjust(n,'0') #오른쪽 정렬(0으로 채워주기)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
