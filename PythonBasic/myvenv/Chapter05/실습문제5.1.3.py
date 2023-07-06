price = int(input("현재 가진 금액을 입력 >>> "))

if price >= 20000:
    print("오늘 저녁은 치킨이닭")
elif price >= 10000:
    print("오늘 저녁은 떡볶이...")
elif price == "":
    print("금액을 입력하세요")
else:
    print("오늘 저녁은 편의점 김밥...")