# 멤버십 연산자
# in, not in
# 특정한 값이 "컨테이너 자료형" 포함이 되어 있는지를 검사

# 리스트와 멤버십 연산자
numbers = [1,2,3,4,5]

for num in numbers:
    if num == 2:
        print('2을 찾았습니다.')
        break

print(100 in numbers)
print(100 not in numbers)

# 딕셔너리와 멤버십 연산자
colors = {'Red':'빨강',
          'Blue':'파랑',
          'Yellow':'노랑'}
print(colors)

# key 모음에 포함될 때만 True
print('빨강' in colors) 
print('Red' in colors)

# value에서 검사하고 싶을 땐, 
# colors.values() 메소드 필요

print(colors.values())
print('빨강' in colors.values())
