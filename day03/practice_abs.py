# 절댓값을 반환하는 함수
num = -3.6
answer = abs(num) # 절댓값 = 양수로 반환
print(answer)

# 1. 사용자 정의 함수로 절댓값을 반환하는 함수 만들기
# abs_func 이라는 함수 만들기
# 선언 (define)
def abs_func(number):
    if number > 0:
        return number
    else:
        return -1*number

answer = abs_func(100)
print(answer) # 절댓값 처리 -> 1 이 나와야 한다.

# 2. 두 수의 차 절댓값으로 만들기
# A와 B 정수를 입력받아 두 수의 차의 절댓값을 반환하는 함수
# abs_diff 를 만들기
# 선언(define)
def abs_diff(a, b):
    c = a - b
    if c > 0:
        return c
    else:
        return -1*c

# 7과 -3을 받았다면 10을 출력해야 한다.
answer = abs_diff(10, -3)
print(answer)