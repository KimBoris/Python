# // -> 몫
#  % -> 나머지
#  ** -> 제곱


x = 5
y = 2
print(x+y)
print(x-y)
print(x*y)
# C#과 다르게 / 에 대한 연산이 이루어 진다 ex) 5/2 = 2.5
print(x/y)

print(x//y)
print(x%y)
print(x**y)



# - 문자열 연산

tag1 = "#내꺼하자\t"
tag2 = "#오늘부터 1일\f"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" *5
print(message)



# - 복합 할당 연산자
level = 10
level += 1

health = 2000
health -= 300



attack = 300
attack *= 1.5


speed = 420
speed /= 2

print(level, health, attack, speed)
