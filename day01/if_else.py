# # 조건문
# # 비교 연산의 결과
# if 2 >= 5: # if False
#     print('조건이 참입니다.')
#     print('같은 들여쓰기 수준이라면')
#     print('동일한 코드블럭입니다.')

# print('무조건 실행됩니다. 조건문과 상관없이')

# # 비교 연산 + 산술 연산 조합
# # 홀수일때만 출력
# number = 3
# if number % 2 == 1: # 2로 나눈 나머지가 1 -> True
#     print(f'{number}는 홀수')
    
# # 논리 연산 결과
# name = '' # False
# if not name:
#     print('이름이 비었습니다.')

# # if 조건:
# #   코드블럭

# # A라면 B하고, A가 아니라면 C하겠다.
# print('===============')
# temperature = 10

# if temperature >= 30: # False
#     print('아이스 아메리카노')
# elif temperature >= 25: # False
#     print('아이스 라떼')
# else:
#     print('따뜻한 아메리카노')


# if 조건1:
    # 조건1 만족 시 실행되는 코드
# elif 조건2:
    # 조건2 만족 시 실행되는 코드
# else:
    # 그 외에 모든 케이스에서 실행되는 코드

age = int(input('나이를 입력해 주세요.:'))
# 나이에 따라, 출력하는 단어를 다르게 해봅시다.
# 1. 20살 이상 어른
# 2. 10살 이상 청소년기
# 3. 5살 이상 어린이
# 4. 영유아기

if age >= 20: # False
    print('어른')
elif age >= 10: # True
    print('청소년기')
elif age >= 5:
    print('어린이')
else:
    print('영유아기')