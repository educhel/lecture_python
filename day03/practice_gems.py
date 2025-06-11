# 제어문, 반복문과 다양한 풀이
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# Q. 채굴한 광물들 중 1등급 광물이 "존재하는지 여부"
# 1. 멤버십 연산자
print(1 in gems)

# 2. for 문 + if 문
for gem in gems:
    if gem == 1:
        print(True)
        break

# 등급 별로 광물이 몇 개 있는데?
# 1. 딕셔너리
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0,2:0,3:0} # 등급별 갯수 세기 위한 딕셔너리

# 방법 1
for gem in gems:
    grades[gem] += 1

print(grades)

# 방법 2
# 비어있는 딕셔너리를 이용한다.
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {}

for gem in gems:
    if gem in grades:
        grades[gem] += 1
    else:
        grades[gem] = 1

print(grades)

# 2. 리스트 (심화)
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = [0,0,0] # [0] * 3

for gem in gems:
    grades[gem-1] += 1

print(grades)