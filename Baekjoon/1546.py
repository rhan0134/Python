# 1546번_평균
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

#1
count = 0

N = int(input())
score = list(map(float,input().split())) #배열에 실수 입력
M = max(score) #실수 최댓값
L_s = len(score) #과목수

for s in range(L_s):
  score[s] = (score[s]/M)*100

for p in score:#점수 다 더하기
  count += p

print(count/L_s)#평균 구하기

#2
N = int(input()) #시험 본 과목의 개수 N
score = list(map(float,input().split())) #배열에 실수 입력
M = max(score) #실수 최댓값
L_s = len(score) #과목수

for s in range(L_s):
  score[s] = (score[s]/M)*100
  
print((sum(score)/L_s))

#3 EX) 3/10*100 + 10/10*100 == (3+10)/100 * 100
N = int(input()) #시험 본 과목의 개수 N
score = list(map(float,input().split())) #배열에 실수 입력
M = max(score) #실수 최댓값
L_s = len(score) #과목수

print((sum(score)/M *100)/L_s)