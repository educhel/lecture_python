# 딕셔너리
# 특징 1 : 순서 없음
# 특징 2 : 가변 자료형 (mutable)

students = {'kyle':10,
            'jun':20,
            'alex':30}

# 값 조회
print(students['kyle']) # key가 존재할 때만 출력됨
# print(students['justin']) # key가 없을 때 KeyError

# 값 조회에 사용되는 메서드
print(students.get('kyle'))
print(students.get('justin','Unkown key')) # None

# 가변 자료형 - 딕셔너리
# 변경 : 추가, 삭제, 수정
# 삭제
students.pop('jun')
print(students.pop('justin',0))

# print(students)

# 조회
print(list(students.keys()))
print(list(students.values()))
print(list(students.items()))