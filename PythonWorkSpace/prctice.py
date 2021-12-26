#정수
print(5) 
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*5)
print(3*(3+1))


#문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 5)


# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

#애완 동물을 소개해주세요
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

#만약 강아지 이름이 해피로 바뀐다면?
#변수를 활용한다.
print("")
animal = "고양이"
name = "사랑이"
age = 4#int형을 사용할때는 str(age) 형식으로 사용해야 한다.
hobby = "배긁기"
is_adult = age >=3 #boolean도 str(is_adult)형식을 사용해야 한다.
print("우리집" + animal +" 의 이름은 " + name + "예요")
print(name + "는" + str(age) + "살이며" + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))
#(+)를 사용하려면 int형 boolean형 str(a)와 같은 형태로 사용해야한다.


# (+)가 아닌 (,)쉼표로도 print문을 사용할 수 있다.
# (,)를 사용하면 str을 사용하지 않는다. 또한 (,)는 띄어쓰기를 하나 포함한다.
# ex) 사랑이 는 어른일까요? 이런식으로 띄어쓰기가 포함됨
print(name, "는 ", age, "살이며, ",hobby, "을 아주 좋아해요")
print(name, "는 어른일까요?",is_adult )

# '''여러 문장에 대해 주석처리를 할때에는 (''')내용(''') 작은 따옴표로 앞 뒤를 지정하면
# 주석 처리가 된다.'''
#Ctrl + /(slash)  >> 주석처리



#########################퀴즈#########################

#변수를 이용하여 다음 문장을 출력

#변수명 : station;
#변수값 : "사당", "신도림", "인천공항" 순서대로 입력
#출력 문장
# : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")




#######################################################



# 연산자
print(1+1) #2
print(3-2) #1
print(6/3) #2
print(5*2) #10

print(2**3) #2^3 = 8 (2의 3승)
print(5%3) #2 나머지
print(10%3) #1

print(5//3) #몫 #1
print(10//3) #몫 #3

#비교 연산도 가능 (참 거짓을 값으로 반환)
print(10>3) #True
print(4>=7) #False
print(10<3) #False
print (5<=5) #True /한가지가 같기 때문에 True를 반환

print(3==3) #True
print(4==2) #False
print(3+4 == 7) #True

print(1 != 3) #True
print(not (1 != 3)) # False - not(1은 3과 같지않다) = False



#두개 이상의 항을 비교 연산
print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True  
#and와 (&)는 같다

#Or
print((3>0) or (3>5)) #True 둘중 하나만 만족해도 True
print((3>0) | (3>5)) #True 둘중 하나만 만족해도 True

print(5>4>3) #True 연속 되는 값도 연산이 가능하다
print(5>4>7) #False

print(2+3*4) #14
print((2+3) * 4) #20

number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)

#이것을 좀더 편하게
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /=2 #18
print(number)
number -= 2#16
print(number)
number%= 5 #1
print(number)



####파이썬에서 제공하는 '숫자 처리 함수'

#1. abs() - 절대값을 반환해준다
print(abs(-5)) #5
#2. pow() - 절대값을 반환해준다
print(pow(4,2)) #4^2 = 16
#3. max() - 최대값을 반환
print(max(5,12)) #12
#4. min() - 최소값을 반환
print(min(5,12)) #5
#5. round() - 반올림
print(round(3.14))
print(round(4.99))


#파이썬의 math라이브러리를 이용하는 방법도 있다
from math import *  #Math라이브러리 안에 있는 모든것을 이요하겠다
#1. Floor() - 내림
print(floor(4.99)) #내림 4
#2. ceil() - 올림
print(ceil(3.14)) #올림 4
#3. sqrt() -  제곱근
print(sqrt(16)) #4
print(floor(31.9))
print(ceil(166.9))
print(sqrt(9))



#랜덤 함수

#난수- 랜덤을 사용할때에는 random
#1 ~0 미만의 임의의 값 생성
from random import *
#random()
print(random())  #0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10) #0.0~ 10.0미만의 임의의 값을 생성하고 10배

#정수값만 보려고 할 때
#int(random())
# +1을 한 이유는 0이 나오지 않게 하기위해
print(int(random() * 10) +1)
print(int(random() * 10) +1)
print(int(random() * 10) +1)

print(int(random() * 45 + 1))#1~45


#randrange(1,46) = 1~45
print(randrange(1, 46)) #1부터 45미만의 값을 생성해라
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

#이것이 헷갈릴때 아래 방법
#randrange(1,46) 1~45까지의 번호
# *1~45이하의 값을 생성해주는 방식



#########################퀴즈#########################

#당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

#조건 1 : 랜덤으로 날짜를 뽑아야 함
#조건 2 : 월별 일 수가 다름을 감안하여 최소 일수인 28이내로 정함
#조건 3 :  매월 1~3일은 스터디 준비를 해야하므로 제외

#from random import *를 작성해줘야한다 (랜덤 함수를 활용하기 위해)
from random import*







#
data = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월" + str(data) + "일로 선정되었습니다.")















#######################################################





