# 변수
# 할당 연산자 (=)
# 변수 이름 = 변수에 저장되는 값 -> 항상 고정
# name = '배지원'   # 문자열 str
# age = 20        # 정수형 int
# is_male = False # 불린형 bool

# print('이름은?')
# print(name)

# print('나이는?')
# print(age)

# print('남자인가요?')
# print(is_male)

# # 변수의 장점
# # 1. 데이터에 의미를 부여한다.
# # 20 숫자의 의미? 나이, 진행율, 돈 ... 
# print(20) # 정보를 알 수가 없다!

# age = 20 # 해석이 명확해진다!
# print(age)

# # 2. 재사용성과 가독성
# print(name)
# print(name)

# print('===================')
# # 변수명 = 값 -> 할당 연산자를 통해 변수에 값을 할당
# # 식별자(identifiers) = 리터럴(literal)

# # 식별자 작성 규칙
# name_1 = 'alex'
# name_2 = 'jun'
# print(name_1, name_2)
# # 중요! 예약어, 내장함수로 지으면 안된다.
# # True = '참' # 할 수 없다.
# # type = '자료형' # 할 수 있지만, 하지 마라!
# # print(type('1'))
# # print(type)

# print(name)
# name = '정우영'

# print(name)

a = [10,20]
b = a

print(a)

# print(id(a))
# print(id(b))

# name = input('이름을 입력해 주세요.')
# print(f'안녕하세요, {name}님!')