a = [1,2,3]

#데이터 추가 - .append(데이터)
#데이터 할당 - 리스트[인덱스] = 데이터
#데이터 삭제 - del 리스트[인덱스]

a.append(4)
print(a)

a[0] = 9
print(a)

del a[3]
print(a)


#슬라이싱  -  리스트[시작:끝 +1]
#리스트 길이  -  len(리스트)
#리스트 정렬   리스트.sort()

b = [3,4,2,1]



print(b[1:3])

print(len(b))

b.sort()
print(b)