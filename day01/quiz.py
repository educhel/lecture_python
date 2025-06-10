# 1. 변수 만들기
# 변수 a 에 문자열 `456` 을 할당하고, 변수 b 에 정수 `789` 를 할당하세요.
# a = "456"
# b = 789
# print(type(a)) # str
# print(type(b)) # int

# # 2. 연산해 보기
# #  456 + 789 = 1,245

# # a 와 b를 더하려 하였을 때 (+), 어떠한 일이 일어나나요?
# # 코드를 추가하여, 수리적 연산을 완료해 봅시다.

# # a + b
# # TypeError: can only concatenate str (not "int") to str

# # str -> int
# # 방법 1 : 변수 재할당
# a = int(a)
# print(a)
# print(type(a))

# print(a + b)

# # 방법 2 : 명시적 형변환
# # 변수를 바꾸는 것이 아닌 계산만 수행
# print(int(a) + b)

# # 3. 식별자와 리터럴
# # 변수의 이름을 식별자라고 합니다. 
# # 아래는 변수를 할당하는 코드인데, 각각 어떠한 문제점이 있을까요? 
# # 왜 이렇게 식별자 이름을 설정하면 안될지 생각해 봅시다.

# # 1
# # 변수명 작성 규칙 -> 숫자가 먼저 올 수 없다.
# number_1 = 1.0 
# print(number_1)

# # 2
# # 내장 함수 print를 문자열이 담긴 변수로 재할당하였기 때문에
# # 더이상 print 함수를 사용할 수가 없어서 에러 발생
# print_exp = "출력을 위한 함수"
# print(print_exp)

# # 
# # 변수 a 에 문자열 `456` 을 할당하고, 변수 b 에 정수 `789` 를 할당하세요.
# # 변수 c는 " " 공백이 있는 문자열이고, d 는 a에서 b를 나눈 몫입니다.

# # 두 변수를 가지고
# # 비교 연산자, 논리연산자를 사용해서
# # True를 반환하는 2개 이상의 케이스를 만들어 내세요.

# a = '456' # str
# b = 789

# c = " "
# # d = a // b # str // int -> error
# d = int(a) // b

# print(c) # " " (str)
# print(d) # 0 (int)

# print(bool(c)) # True -> 공백이라도 값이 하나 있기 때문!
# print(bool(d)) # False -> 0 이기 때문에 비어 있다고 해석

# # 비교 연산자
# # ==, != : 단순비교 -> 값이 일치하는지 판단
# # <=, >=, >, < : 대소비교 -> 값의 크고 작은 여부를 판단
# # -> True / False

# print(type(c))
# print(type(d))

# print(c != d) # True (1)

# # 논리 연산자
# # and, or, not -> 논리값들끼리 연산 
# # a and b, a or b, not a
# # 불린형으로 해석될 수 있는, 연산의 결과가 불린형이 되는!
# print(not c == d) # True (2)
# print(not d)      # True (3)
# print(c != d and not d) # True (4)

# [백화점 VIP 판별 프로그램]
# VIP : 1000만원 이상 소비하면서, 구매 횟수 10번 이상인 경우
# 우수 : 둘 중 하나라도 만족하면, 우수
# 일반 : 둘 다 없으면 일반 고객

money = float(input('소비금액 (단위:만원)')) #float -> 숫자
count = int(input('구매 횟수')) # int -> 숫자

condition1 = money >= 1000
condition2 = count >= 10

if condition1 and condition2: # False
    print('VIP 회원입니다.')
elif condition1 or condition2: # True
    print('우수 회원입니다.')
else:
    print('일반 회원입니다.')