data = []
result = int(input("1일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("2일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("3일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("4일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("5일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("6일차 턱걸이 횟수>>>"))
data.append(result)
result = int(input("7일차 턱걸이 횟수>>>"))
data.append(result)

print(data)
total = data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]
print(total)

for i in range(1, 6):
    print(int(input(i+ "일차 턱걸이 횟수 >>>")))



