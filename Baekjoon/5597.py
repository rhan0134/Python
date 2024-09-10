# 5597번_과제 안 내신 분..?
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

#1 리스트에서 있는 출석번호를 빼는 방법
id_m = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for num in range(28):
    id_s = int(input())
    for i in id_m:
        if i == id_s:
            id_m.remove(i)

print(id_m[0])
print(id_m[1])

#2 없는 출석번호를 다른 리스트에 넣는 방법
li_Y = []
li_N = []

for i in range(28):
  li_Y.append(int(input()))

for i in range(1,31):
  if i not in li_Y:
    li_N.append(i)

print(min(li_N))
print(max(li_N))

#3 1번 방법에서 조금 더 효율적으로 리스트를 생성
li = [i for i in range(1,31)]

for i in range(28):
    num = int(input())
    for j in range(len(li)):
        if li[j] == num:
            li.remove(num)
            break

print(min(li))
print(max(li))