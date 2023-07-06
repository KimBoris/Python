result  = [33, 40, 12, 63, 52]

# 1. 6번 9개 추가
result.append(6)
print(result)

# 2. 2번은 재측정하여 50개 함 ( 데이터 변경해보자)
result[1] = 50
print(result)

# 3. 3~6번까지 데이터를 슬라이싱

print(result[2:])

# 4. 오름차순 정렬
result.sort()
print(result)
