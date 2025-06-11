# 함수 기초
print('===함수 사용 전===')
number1 = 5
number2 = 10

# 둘 중 뭐가 큰지 비교
if number1 > number2:
    answer = number1
else:
    answer = number2

print(answer)

number3 = 7
number4 = 4

# 뭐가 큰지 비교
if number3 > number4:
    answer = number3
else:
    answer = number4

print(answer)

print('====함수 사용 후====')
# 함수 정의(define)
# 함수라고 하는 블럭을 만든다.
def get_bigger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# 박스만 만든 것이기 때문에 "아무일도 일어나지 않는다."

# 함수 호출 (call)
# 함수를 불러와서 사용하는 것을 의미합니다.
print(get_bigger(number1,number2))
print(get_bigger(number3,number4))