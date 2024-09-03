# 2588번_곱셈

#1
A = int(input())
B = int(input())
B3 = B//100
B2 = B%100//10
B1 = B%10
print(A*B1)
print(A*B2)
print(A*B3)
print((A*B1)+((A*B2)*10)+((A*B3)*100))

#2
A = int(input())
B = input()

for i in range(2,-1,-1):
    print(A*int(B[i]))

print(A*int(B))