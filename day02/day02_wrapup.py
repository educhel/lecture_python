# 컨테이너 자료형
# 리스트 (list)

greetings = ['안녕','니하오','봉주르','올라']
print(greetings)
print(type(greetings)) # <class 'list'>
print(len(greetings)) # 4

# + 연산, * 연산
# + : 이어 붙인다. 리스트끼리
print(greetings + greetings) 
# * : 이어 붙인다. 같은 리스트를 n번
print(greetings * 2)
# => 연산의 결과, 새로운 리스트를 만든다.

# 리스트 특징 1: 순서 있다.
# 순서(위치)로 값에 접근이 가능
print('==인덱싱/슬라이싱==')
print(greetings)
# 인덱싱     0 1 2 .... n-1 (길이-1) 까지 가능
# 음수인덱싱  -n ...... -2,-1 (뒤에서부터 인덱싱 가능)
print(greetings[2])   # 위치로 인덱싱이 가능
print(greetings[1:3]) # 슬라이싱도 가능
print(greetings[::-1]) # 뒤집기 가능

# 리스트의 특징 2 : 가변 자료형 (mutable)
# 변경 -> 추가, 수정, 삭제 가능
# 리스트의 주소값을 바꾸지 않고도 가능 -> 그대로 객체 주소를 유지하면서도 변경 가능 하다.

# 원소 수정
print(f"수정 전 인삿말 : {greetings}")
print(f"수정 전 주소 : {id(greetings)}")
greetings[0] = '좋은 아침!'
print(f"수정 후 인삿말 : {greetings}")
print(f"수정 후 주소 : {id(greetings)}")

# 원소 추가
greetings.append('곤니찌와')
# greetings[4] = '곤니찌와' # index out of range

print(f"추가 후 인삿말 : {greetings}")
print(f"추가 후 주소 : {id(greetings)}")

# 원소 삭제
greetings.pop(2)
print(f"삭제 후 인삿말 : {greetings}")
print(f"삭제 후 주소 : {id(greetings)}")

print('====문자열====')
# 문자열 특징 1: 순서가 있다.
hello = '안녕하세요! 오늘도 좋은 아침입니다.' #
print(hello)
print(type(hello))

print(len(hello))
print(hello[6]) # 인덱싱 가능 
print(hello[1:6]) # 슬라이싱 가능

# 문자열 특징 2: 불변 자료형 (immutable)
# hello[-1] = '~' # TypeError
print(id(hello))
hello = hello[:-1] + '~'
print(hello)
print(id(hello))


# 반복문
# for문 : 반복횟수가 정해져 있을 때
print('====반복문====')
print(greetings)

# 예시 1 - 리스트가 올 수 있다.
for greeting in greetings:
    print(greeting)

# 예시 2 - range도 올 수 있다.
for i in range(len(greetings)):
# for i in range(4): 와 같다! 
# -> range(4) 정수 목록을 반환 0 ~ N-1 정수목록 반환
    print(i)
    print(greetings[i])

# for문의 대상이 될 수 없는 것 -> 순회 불가능
# for i in 3.3: # TypeError: 'int' object is not iterable
#     print('안됩니다.')

# while문 : 반복횟수가 정해져 있지 않을 때, (조건)을 기준으로 반복함
i = 0 # 생성

while i < len(greetings):
    print(greetings[i])
    i += 1