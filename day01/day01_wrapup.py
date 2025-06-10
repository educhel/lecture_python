# 1일차 복습
# 변수 = 상자 (사실은 상자 아님)
# 할당 연산자 = 을 통해 변수를 할당함
print('====변수===')
name = 'alex' # 이제부터 name이라는 변수를 부르면, alex가 튀어 나온다!

print('alex')
print(name)
# 변수는 사용자가 사용하기 편하라고 만든다.
variable1 = 10
variable2 = 30 # 의미 없는 변수

age = 10
money = 30 # 변수명을 설정할 때는 의미를 담아야 한다.

print(f'안녕하세요, {age}살의 {name}님! 오늘도 화이팅!')

# 재할당
name = 'jun' # 가장 마지막에 할당한 값이 들어있게 된다.
print(f'안녕하세요, {age}살의 {name}님! 오늘도 화이팅!')

# 자료형
# 자료형이란? 데이터의 특성
print('===자료형===')
name = 'alex'
age = 20
money = 30.0
is_male = True

# 1. 숫자
print(type(age))   # int : 정수형  (0,1,-1)
print(type(money)) # float : 실수형 (소수점이 있는 모든 숫자)

# 2. 문자열
# "", ''를 통해 글자들의 모음을 만든다.
# 쌍따옴표, 따옴표 안에 들어있는 모든 것이 문자열이 된다.
print(type(name)) # str : 문자열

print('') # 비어있는 문자열도 문자열 -> ""
print(" ") # 공백이 있는 문자열도 문자열 -> " "

# 3. 불린형
# 참(True) / 거짓(False)
# true # 불린형이 아님! -> 대소문자 유의
print(is_male)
print(type(is_male)) # bool

# 형 변환
# 내장함수 사용하여 변환
# int(변환하고 싶은 값)
# float(변환하고 싶은 값)
# str(변환하고 싶은 값)
# bool(변환하고 싶은 값)
print(type(int('3')))     # 가능
# print(type(float('3/5'))) # 불가능

# 연산자
# '처리'
print('===연산자===')

# 1. 산술 연산자 (+,-,*,/,//,%,**) -> 숫자 계산
# 2. 복합 연산자 (+=,-=,*=,/=,//=,%=,**=) -> 산술 연산 후, 재할당

# 3. 비교 연산자
# 값 두개를 "비교" -> True / False
# 대소 비교 : <, >, <=, >= (수치 자료를 위주로 사용하는 게 이해가 쉬움)
# 일치 비교 : ==, != (자료형을 크게 타지 않는다.)
a = True
b = 'False'
print(a != b)
# 조건문 / 반복문 하단에서 비교연산을 많이 사용하겠습니다!

# 4. 논리 연산자
# a and b : True, True -> True 그외, False
# a or b : 어느 하나라도 True 면 True
# not a  : 반대
print(name == 'alex')
print(money > 100)

# 조건문
print('===조건문===')
name = 'jun'

print(name)
print(money)

if name == 'alex' and money > 10: # False
    print('부자 alex, 안녕하세요!')
elif name == 'alex': # True
    print('alex 안녕하세요!')
else:
    print('누구세요?')
    # print('장난입니다~') # 1번 케이스

print('장난입니다~') # 2번 케이스 
# -> 들여쓰기에 따라 의도와 다르게 작동할 수 있다.