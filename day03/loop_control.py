# 반복문 제어
# break
print('===break===')
numbers = [1,2,3,4,5]
print(f'numbers의 길이 : {len(numbers)}')

for n in numbers: # 전체를 모두 실행
    print(n)
    
    if n == 3:
        print('반복을 종료합니다.')
        break
        print('break문 이후 문장을 결코 실행되지 않아요!')

# else
print('===else===')
numbers = [1,2,3,4,5]

for number in numbers:
    if number == 30:
        print('30을 찾았습니다!')
        break
else:
    print('30을 찾지 못했습니다.')

# print('30을 찾지 못했습니다.')
# 30을 찾았던, 찾지 못했던 상관없이 무조건 출력이 됩니다.

# continue
print('===continue===')

number = 0

while number <= 5:
    number += 1
    
    if number % 2 == 0: # 짝수인 경우만, 건너 뛰기
        continue
    
    print(number)

print('===pass===')

# def solution(number):
#     pass

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
    
    if number == 3:
        pass