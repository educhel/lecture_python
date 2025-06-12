# <별 찍기>
# 자연수 N을 입력받아, N줄까지 "별을 출력하는" 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

# 선언 (define)
# 매개 변수 o, 반환값 x
def print_star(n):
    for i in range(1,n+1):
        print('*'*i)

# 호출 (call)
# 올바른 호출법
n = int(input('정수를 입력해 주세요.:'))
print_star(n)

# 잘못된 케이스 1
# 입력 받아야 하는데, 입력 받지 못함
# print_star() # 에러 발생

# 잘못된 케이스 2
print(print_star(n))
# 반환되는 값이 없는데, 값을 달라고?
# 파이썬에서 자체적으로 없다 "None"