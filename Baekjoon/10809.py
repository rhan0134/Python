# 10809번_알파벳 찾기
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#1 아스키 코드 이용해서 비교
li = []
S = input()
for i in range(97,123): 
  n = -1
  for s in range(len(S)):
    if S[s] == chr(i):
      n = s
      break
  li.append(n)
print(*li)

#2 'in' 사용
S = input()
W = 'abcdefghijklmnopqrstuvwxyz'

for w in W:
    if w in S:
        print(S.index(w), end=' ')
    else:
        print(-1, end=' ')

#3 'find' 사용
S = input()
for i in range(97,123):
    print(S.find(chr(i)), end = ' ')
    

