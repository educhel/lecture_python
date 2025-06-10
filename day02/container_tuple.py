# 튜플
# <class 'tuple'>
# 순서가 있는 컨테이너 자료형
# 불변 자료형

# () -> 내부의 값들을 입력 / 각 값은 ,를 통해 구분
numbers = (10, 20, 30, 40, 50)
print(numbers)
print(type(numbers))

# 연산 가능 (+, *)
# 연산 후에는 새로운 튜플을 만들어 낸다.
numbers1 = (1,2)
numbers2 = (3,4)
numbers3 = numbers1 + numbers2
print(numbers3)
print(id(numbers1))
print(id(numbers2))
print(id(numbers3))

print(numbers1*3)

# 튜플의 특징 1 : 순서가 있는 자료형
print('===인덱싱===')
print(numbers)
print(numbers[-1])

print('===슬라이싱===')
print(numbers[1:3])

# 튜플 특징 2: 불변 자료형
# 불가능하다. 변경이

# numbers[0] = -1
# TypeError: 'tuple' object does not support item assignment