# 9498번_시험 성적
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

A = int(input())

if A<=100 and A>=90:
    print("A")
elif A<=89 and A>=80:
    print("B")
elif A<=79 and A>=70:
    print("C")
elif A<=69 and A>=60:
    print("D")
else:
    print("F")