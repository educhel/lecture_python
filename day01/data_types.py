# 자료형
# 1. 숫자
# 1) 정수
print(1)
print(-3)
print(0)
print(type(0))

# 2) 실수
# 소수점이 포함된 숫자
print(3.141592)
print(type(3.141592))

# 질문
print(type(3.0)) 
# <class 'float'>
# 소수점 여부에 따라 float 가 된다.

# 2. 문자열
print("강우진")
print('하선혜')
print(type("송연준")) # <class 'str'>

# 에러 발생
# print("이한별')

print('')
print(" ")
print(type("")) # 공백도, 빈 문자열도 문자다!
print(type(" "))

# 따옴표 안에 따옴표를 쓸 때는 서로 다른 종류를 써줘야 한다.
print("오늘은 '월요일'입니다.")
print('내일은 "화요일"입니다.')
# \를 통해 따옴표가 따옴표로 역할 하지 않게 할 수도 있다.
print("모레는 \"수요일\"입니다.") 

print('123')
print(123)
print(123 == '123') # 비교 연산
print(type('123'))
print(type(123))

# 문자열 포맷팅 - f-string
name = '배지원'
age = 20
sentence = f"{name}은 {age}살입니다."
print(sentence)

# 3. 불린형 (boolean)
# True, False
print(True)
print(False)
print(type(True)) # <class 'bool'>

# 자료형 정리
# 1. 숫자 : 정수(int) / 실수(float)
# 2. 문자 : 문자열(str) -> "12412#!@#$@    ", '문자들의 모음'
# 3. 불린 : 불린형(bool) -> True, False (대소문자 구분 주의)

# 명시적 형변환
# 정수형으로 변환 : int(   )
print(1.25)
print(int(1.25))
print(type(1.25))
print(type(int(1.25)))

print('20')
print(20)
print(type('20'))
print(type(20))

# 정수로 변환될 수 있는 형식일 때만가능하다.
# print(int('20.0'))
# print(type(int('20.0')))

# 실수형 변환 : float(    ) 
print(float(-10)) # 정수를 실수로
print(float('20.0'))
print(type(float('20.0'))) # 문자열을 실수로

# 문자열 변환 : str(   )
print(str(1234))
print(type(str(1234))) # 정수를 문자열로

print(type(3.141592))
print(type(str(3.141592))) # 실수를 문자열로

print(True)
print(False)
print(str(True))
print(type(str(True)))

# 불린형 : bool(   )
# True / False

print(bool(0.0000000000001))

# 자료형
# 1. 숫자형
# 정수 (int) : 소수점이 없는 숫자 (0,양,음)
# 실수 (float) : 소수점이 있는 숫자 (2.1, 0.0)

# 2. 문자형 (str)
# 문자의 형태를 가진 모든 글자들의 모음
# 쌍따옴표 "", 따옴표 '' 를 통해 만든다. (짝이 맞아야 함)
# 만약 따옴표 안에 따옴표를 쓰고 싶다면? 
# 다른 따옴표를 쓰거나 이스케이프 문자열(\)을 쓴다.

# 3. 불린형 (bool)
# 참(True) / 거짓(False) -> 대소문자 주의

# 각각의 자료형은 내장함수 int(),float(), str(), bool() 을 통해 
# 명시적 형변환을 할 수 있다.

