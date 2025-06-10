# for 반복문
# 반복 횟수가 정해져 있을 때, 사용한다.

# 기본 사용법
# for 변수 in 컨테이너:
    # 반복 코드

# 1. 리스트 순회하기
names = ['ken','jun','justin']
print(len(names)) # 컨테이너의 길이를 알 수 있는 내장함수

for name in names:
    print(f'안녕하세요, {name}님!')

print(name)

# 2. 문자열 순회하기
word = 'python'
print(len(word))

for character in word:
    print(character)

# 3. 조건문 함께 사용하기
numbers = list(range(1,11))
print(numbers)

for number in numbers:
    if number % 2 == 0: # 짝수인 경우에만
        print(number)

# RANGE를 이용한 정수 목록
for number in range(1, 11):
    if number % 2 == 1: # 홀수인 경우에만
        print(number)
        
# for 문 간단 실습 문제
# for문, range를 활용하여 1~10 더한 값 55 출력하기

print('for 문 간단 실습 문제')
answer = 0

for i in range(1,11):
    # range를 순회하며, i 에 순서대로 할당
    answer = answer + i # 복합 연산자 += 을 통해 재할당 가능
    print(f'answer의 변화 : {answer}')
    
print(answer)

# 조건에 따라서 합산도 가능

answer = 0

for i in range(1,11):
    if i % 2 == 0: # 짝수인 케이스만
        answer += i
        print(f'answer의 변화 : {answer}')

print(answer)