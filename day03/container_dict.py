# 순서가 없는 컨테이너
# 딕셔너리

user = {'name':'jun',
        'age':20,
        'license':True}
print(user)

# 딕셔너리 특징 1 : 순서가 없다.
# key:value의 쌍으로 이루어져 있다.

# key는 유일해야 한다. key는 바뀔 수 없다.
# -> 바뀔수 없는 자료형을 써야 한다. (immutable)

# 접근
# key를 기준으로 인덱싱하여 value에 접근한다.
print(user['age'])

# 딕셔너리 특징 2 : 가변 자료형 (mutable)
# 값을 변경해도 똑같은 주소(id)를 가진다

# 수정
print(id(user))
user['age'] = 30
print(user)
print(id(user))

# 추가
# 할당으로 새로운 key-value를 추가할 수 있다.
user['is_male'] = True
print(user)

# 삭제
user.pop('license')
print(user)

# 딕셔너리 메서드

# key만 확인하기
print(user.keys())
print(list(user.keys()))

# value만 확인하기
print(user.values())
print(list(user.values()))

# key와 value를 한번에 보기
# key:value의 역할을 무시하고, (쌍을 제거하고) 튜플로 반환
user_list = list(user.items())
print(type(user_list[0]))
print(user_list[0])
print(user_list[0][0])
