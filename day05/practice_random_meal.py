# 랜덤 밥먹기
import random
import time

students = ['성우님', '민지님', '주용님', '현근님', 
            '나라님', '민석님', '연준님', '근찬님',
            '재룡님', '한별님', '정원님', '혜지님', 
            '승찬님', '재훈님', '유정님', '우진님']

# students가 다음과 같이 주어졌을 때,
# 랜덤 밥먹기 조를 배정하는 프로그램을 짜 보세요!
print(students)

# 방법 1
# random -> sample
team = []
for i in range(len(students)//4):
    people = random.sample(students, 4)
    team.append(people)
    
    for person in people:
        students.remove(person)

print(team)
print(len(team))

# 방법 2 - random
students = ['성우님', '민지님', '주용님', '현근님', 
            '나라님', '민석님', '연준님', '근찬님',
            '재룡님', '한별님', '정원님', '혜지님', 
            '승찬님', '재훈님', '유정님', '우진님']

team = {}
for i in range(1,5):
    team[i] = []

available_team = list(range(1,5))

for student in students:
    team_num = random.choice(available_team)
    team[team_num].append(student)

    if len(team[team_num]) >= 4:
        available_team.remove(team_num)

print(team)

# 방법 3 - shuffle
students = ['우진님','연준님','준수님','한별님',
            '용혁님','혜지님','정원님','승찬님',
            '상준님','근찬님','민석님','성훈님',
            '재훈님','주용님','선혜님','재룡님',
            '나라님','민지님']

for i in range(5):
    time.sleep(1)
    print(f'{5-i}초 남았습니다.')
print('=======오늘의 랜덤 밥먹기=========')

random.shuffle(students)

team_size = 4
team_lst = []

for idx in range(0,len(students),team_size):
    team_lst.append(students[idx:idx+team_size])

print(team_lst)