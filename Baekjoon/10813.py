# 10813번_공 바꾸기
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

#1
N, M = map(int,input().split())
li = []
for n in range(N):
  li.append(n+1)

for p in range(M):
  i,j = map(int,input().split())
  li[i-1], li[j-1] = li[j-1], li[i-1]

print(*li)

#2
# N-바구니 갯수, M-공 바꾸는 횟수
N,M = map(int, input().split())

# 바구니에 적혀 있는 번호와 같은 번호가 적힌 공이 들어있음
li = [i for i in range(1,N+1)]

for m in range(M):
    i,j = map(int, input().split())
    # i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다
    li[i-1], li[j-1] = li[j-1], li[i-1]

print(*li)