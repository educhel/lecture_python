# 4일차 복습
# 함수 (function)
students = ['주용','재훈','유정','현근'] # 리스트

# 1. 사용자 정의 함수
# 1단계 : 정의하기 (define)
def check(student_list,name): # 매개변수
    if name in student_list:
        answer = f'{name}님은 출석하셨습니다.'
    else:
        answer = f'{name}님은 출석하지 않으셨습니다.'
    return answer  # 반환값 문자열

# 2단계 : 호출하기 (call)
answer = check(students,'한별')
print(answer)

# 2. 내장 함수
print(students) # 터미널 상에 출력
print(f'1분단 학생 수는 {len(students)}명입니다.') 
# 길이를 반환하는 내장 함수

# print(sum(students)) # 에러 발생
# 모든 함수가 모든 자료형에 사용 가능한 것은 아니다.

# len 함수
new_students = [['주용','재훈','유정','현근','재룡'],
            ['연준','우진','한별','혜지','정원'],
            [],
            {},
            0.0]
print(len(new_students))

# sorted 함수
# sorted : 정렬된 새로운 리스트를 반환
# 기본적으로 오름차순 정렬
print(students)
students_a = sorted(students,reverse=True)
print(students_a)

print(sorted('python'))


# 컨테이너 자료형 - 리스트
# 1. 순서가 있다.
# 2. 변경 가능하다. -> 가변 자료형 (mutable)
# 값 추가

print(students)
print(id(students))

students.append('재룡') # 자료형에 딸려있는 함수 = 메서드
print(students)
print(id(students))

# 익명함수 lambda
# 사용자 정의 함수 중, 이름을 붙일 필요가 없다고 생각
# -> 일회성으로 사용하는 함수
answr = (lambda x:-x)(-1)
print(answr)

example = [(0, 2), (2, 3), (1, 4), (0, -1)]
print(len(example))
print(type(example))

print(len(example[0]))
print(type(example[0]))

example_a = sorted(example)
print(example_a)

example_b = sorted(example, key=lambda x:-x[1])
# [(0, 2), (2, 3), (1, 4), (0, -1)]
# 첫 번째 (0, 2) -> -2 (이걸 기준으로 정렬)
# 두 번째 (2, 3) -> -3
# 세 번째 (1, 4)-> -4
# 네 번째 (0, -1) -> 1 
# 람다함수를 거쳐서 나온 값을 기준으로 "오름차순"
# [(1, 4), (2, 3), (0, 2), (0, -1)]

print(example_b)

# 리스트 
# 순서 o, 변경 o
numbers = [10,20,30,40,50]

# 추가 -> 순서가 있게 추가 (가장 맨 끝에)
numbers.append(60) 
# 나 자신을 바꾸어 버리면 되기 때문에
# 반환하는 것이 없다.

print(numbers)

# 인덱스 기준
# 삭제 - 위치를 기준으로 삭제
numbers.pop(1)
print(numbers)

# 추가 - 위치를 기준으로 추가
numbers.insert(1,200)
print(numbers)

# 추가 - 여러개의 값을 추가
# numbers.append(1,2,3,4) # 에러
# numbers.append([1,2,3,4])
# print(numbers)

numbers.extend([1,2,3,4,5])
print(numbers)

# 삭제 - 값을 기준으로 삭제
# 없는 경우는 에러 발생
numbers.remove(10)
print(numbers)

# 정렬
numbers.sort()
print(numbers)


# 세기 값을 기준으로 count
cnt = numbers.count(1)
print(cnt)

gems = [1,2,3,3,2,3,3,1]

print(gems.count(1))
print(gems.count(2))
print(gems.count(3))

# 해당하는값의 위치를 반환
print(gems.index(1))
# 가장 첫 번째 나타난 값의 위치 나타내 줌


