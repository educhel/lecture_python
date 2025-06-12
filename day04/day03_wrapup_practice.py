# 딕셔너리 > 'information': 리스트 > 딕셔너리
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

# 구조 확인하기
print(type(users))
print(users.keys())
print(users['total_user']) # int
print(type(users['information'])) 

# 사람들의 정보만 뽑아보기
infos = users['information']
print(infos[0])

# 1. 라이센스가 있는 인원들의 숫자 구하기 (세기)
cnt = 0

for info in infos:
    if info['license']:
        cnt += 1

print(f'라이센스가 있는 인원 : {cnt}명')

# 2. 모든 사람의 나이의 평균 구하기

# 방법 1 : 숫자형 변수와 복합연산 활용
age_sum = 0
for info in users['information']:
    age_sum += info['age'] # 복합연산

ave_age = age_sum/users['total_user']
print(f'나이의 평균은 {round(ave_age,2)}살입니다.')

# 방법 2 : 리스트와 내장함수 활용
age_lst = []
for info in infos:
    age_lst.append(info['age'])
print(sum(age_lst)/len(age_lst))

# 3. 라이센스가 없는 사람들의 이름 모으기
name_lst = []

for info in users['information']:
    if info['license'] == False:
        name_lst.append(info['name'])

print(name_lst)

# 구조화되어 있는 형태의 장점
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

# 추가 레코드
users['total_user'] += 1
users['information'].append({'name': 'ken', 'age':10, 'license':False})
print(users)