# 행렬의 덧셈
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 내 풀이(append 사용)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)   
    return answer


num = int(input())

arr1 = []
for i in range(num):
    arr1.append(list(map(int,input().split())))

arr2 = []
for i in range(num):
    arr2.append(list(map(int, input().split())))

print(solution(arr1, arr2))

# 다른 사람 풀이(zip)
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer