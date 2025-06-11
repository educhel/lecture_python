# 딕셔너리 실습
# 1. 생성
# 여러분들의 정보를 담은 user 딕셔너리를 생성해 주세요.
# 이 때, name, age(한국나이), city, is_male 의 정보를 담아 주세요.
user = {'name':'배지원',
        'age':20,      # int형으로 value
        'city':'seoul',
        'is_male':False
        }
print(user)

# 2. 수정
# 실수로 age의 값을 한국나이로 적었습니다. 
# 만나이를 기준으로 수정해 주세요.
# user['age'] = 19 # 방법 1:재할당
user['age'] -= 1   # 방법 2:복합연산
print(user)

# 3. 추가
# 운전 면허 보유 여부를 나타내는 license 에 정보를 담아주세요.
user['license'] = True
print(user)

# 4. 삭제
# 우리 모두 city는 서울로 동일합니다.
# city의 정보를 삭제해 주세요.
user.pop('city')
print(user)

print(len(user))
print(type(user))