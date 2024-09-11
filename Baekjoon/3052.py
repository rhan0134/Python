# 3052번_나머지
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

#1
li = []
count = 0
for i in range(10):
  N = int(input())
  N %= 42
  li.append(N)

# 정렬해서 크기 비교하는 것
li.sort()
for i in range(9):
  if li[i] == li[i+1]:
    count += 1

print(10-count)

#2
li = [int(input())%42 for i in range(10)]
li = set(li) #집합으로 바꾸어 공통된 값 없애기
print(len(li))