# 기초 자료 구조와 로직 설계
user = ['alex', 3, True]
print(user)

# 순서가 있는 자료 구조 -> 순서로 접근하여 값을 관리
print(user[0]) # "이름" 임을 사용자가 알고 있어야 함
print(user[1]) # "나이" 임을 사용자가 알고 있어야 함
# => 올바르지 않은 자료 구조

# 딕셔너리 
# 순서가 없다
# key : value의 한 쌍의 구조
user = {'name':'alex',
        'age':3,
        'license':True} 
print(user)
print(type(user))
print(user['age'])
