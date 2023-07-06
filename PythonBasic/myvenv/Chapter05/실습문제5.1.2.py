studyTime = int(input("공부시간을 입력하세요(시간) >>> "))

if studyTime >= 10:
    print("휴대폰 잠금이 해제됩니다")
elif studyTime >= 5:
    print("휴대폰 30분 사용 가능")
else:
    print("휴대폰 사용이 불가능합니다.")