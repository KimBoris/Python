korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>> "))

total = korean + math + english
average = total/3


#1
if 0<= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
    if average > 80:
        print("합격")
    else:
        print("불합격")


else:
    print("잘못 입력하셨습니다.")

