# 11720번_숫자의 합
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

sum = 0
N = int(input()) #Python에선 사용하는 부분 X
s = input()
for i in s:
  sum+=int(i)
print(sum)