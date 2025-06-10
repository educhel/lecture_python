# 컨테이너 자료형
# 순서가 있는 컨테이너 - 리스트
# 리스트, <class 'list'>

numbers = [10, "20", 30.0, 40, 50, True, []]
print(numbers)
print(type(numbers))

# 비어있는 리스트도 리스트다
empty = []
print(empty)
print(type(empty))

# 리스트 연산
# + 연산 : 리스트끼리 연결하여, "새로운 리스트" 생성
number_1 = [1, 2]
number_2 = [3, 4]
print(number_1 + number_2)

print(numbers + number_1)

# * 연산 : 같은 리스트를 n번 반복해서 합쳐서 "새로운 리스트" 생성
print(numbers * 2)

# 리스트 특징 1 : 순서가 있는 자료형
# 인덱싱 = 인덱스 (index) -> 위치를 기준으로 원소에 접근한다.
print('====인덱싱====')
# 순서 = 0 부터 시작한다!

# 인덱스     0 , 1,  2,  3,  4 
# 음수 인덱스 -5, -4, -3, -2, -1
numbers = [10, 20, 30, 40, 50]
print(id(numbers))
print(numbers[-1])

# 슬라이싱
print('====슬라이싱====')
print(numbers[1:3])

# 리스트 뒤집기
print(numbers[::-1])
print(numbers)


# 리스트의 특징 2 : 가변 자료형 (가능하다, 변경이)
# 변경이 가능한 자료형 이기 때문에 '수정, 삭제, 삽입' 등등
# -> 객체 자체의 주소가 바뀌지 않는다.

print('===변경 가능===')
# 수정
numbers[1] = -1
print(numbers)
print(id(numbers))

# 추가
# 리스트 마지막 위치에 추가 (기존값을 수정하진 X)
numbers.append(60)
print(numbers)
print(id(numbers))

# 삭제
last_value = numbers.pop()
print(numbers)
print(last_value)
print(id(numbers))