# 윤년 판별 프로그램

year = int(input('연도를 입력해 주세요. :'))
print(type(year)) # <class 'int'>

if year % 4 == 0 and year % 100 != 0:
    # 1. 4의 배수 이면서 100의 배수가 아닌 케이스
    print('Leap Year')
elif year % 400 == 0:
    # 2. 400의 배수인 케이스
    print('Leap Year')
else: # 3. 그외
    print('Not Leap Year')