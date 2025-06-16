# 예외처리
# try : 일단 해봐!
# except : 을 제외하고!

# 예외 처리 하지 않았을때, 
# 에러가 발생하면 무조건 프로그램 종료됨
# n = int(input('숫자를 입력해 주세요!'))
# answer = 10 / n

# print(answer)

# 예외처리를 했을 때, 
# 프로그램이 정상 종료되도록 처리할 수 있다.

try:
    n = int(input('숫자를 입력해 주세요!'))
    answer = 10 / n
except Exception as e: 
    print(f'에러 발생 : {e}')
else:
    print(answer)