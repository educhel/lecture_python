# 연산자
# 처리를 하기 위함이다.

# 1. 산술 연산자
print('====산술연산자===')
a = 5
b = 2

# 사칙연산 (덧셈,뺄셈,곱셈,나눗셈)
print(a + b) # 7 -> int
print(a - b) # 3 -> int
print(a * b) # 10 -> int
print(a / b) # 2.5 -> float

# 몫, 나머지, 제곱
print(a // b) # 2
print(a % b)  # 1 ... 뒤에 붙은 나머지
print(a ** b)

# print(12/0) # 수학적으로도 못하는 것은 파이썬도 못한다.

# 2. 복합 연산자
# a = a + b -> 너무 길다!
# 산술 연산자 & 할당 연산자를 함께 쓰는 것
# += , -=, *=

# a += 1
# b -= 1
# a *= b

print('===복합 연산자===')
print(a, b)

a += b
print(a, b)

a += b
print(a, b)

# 비교 연산자
# 값과 값을 비교한다. -> True, False의 불린 값이 결과로 도출된다.
# A와 B를 비교! 딱 두개만 비교!

print('====비교 연산자====')
print(a, b)
print(a < b) # b가 크다면? True / b가 크지않다면? False
print(a > b) # a가 크다면? True
print(a <= b) # 작거나 같다.
print(a >= b) # 크거나 같다.
# 무엇이 맞는가에 대한 고민이 든다면? 
# 일단 실행해봐라. (<= / =>) ?
print(a <= b)

print(a == b) # a와 b가 같다면, True / 그렇지 않으면 False
print(a != b) # a와 b가 같지 않다면, True /그렇지 않으면 False

# 비교 연산의 경우,
c = 'abc'
d = 'def'
print(c < d) # 다른 자료형도 비교가 가능하다.
print(a != c)

# 4. 논리연산자
# and, or, not
# a를 논리형으로 해석 / b도 논리형으로 해석 => and 연산

print('===논리연산자===')
print(a,b,c,d)
# a and b -> 둘다 True여야만 True
print(a > b) # True
print(c == d) # False
print(a > b and c == d) # True and False -> False

condition_1 = a > b # True
condition_2 = c == d # False
print(condition_1 or condition_2) # True or False

print(not condition_1)

print(True or dkfjlkjlkjdf)
print(False and sdfkjalskdlfk) # 단축 평가 극단적 예시

# 연산자 정리
# "처리"

# 1. 산술 연산자 (+,-,*,/,//,%,**) -> 수치 계산
# 2. 복합 연산자 (+=, -=, *=, ... 산술연산자 모두 제공)
# 3. 비교 연산자 (==, !=, <=, >=, <, >)
# 4. 논리 연산자 (and, or, not)