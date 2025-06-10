# 문자열
# 0개 이상의 문자를 순서가 있게 저장하는 컨테이너 자료형이다.

print('====문자열====')
name = 'python'
print(name)
print(type(name))

# 문자열 특징 1 : 순서가 존재한다.
# 인덱스 (위치)로 값을 확인할 수 있다.
# 값 조회
print(name[2])

# 슬라이싱
print(name[0:2])

# 연산이 가능하다.
# + 연산 : 문자열 + 문자열
# 연산 결과, 새로운 문자열이 생긴다.
word1 = 'hello'
word2 = 'python'
print(word1 + word2)

# * 연산 : 문자열 * 반복 횟수(숫자)
# 연산 결과, 새로운 문자열이 생긴다.
print(word2 * 3)

# 문자열 특징 2 : 불변 자료형
# TypeError: 'str' object does not support item assignment
# word1[0] = 'C' 
word3 = 'C' + word2[1:]
print(word3)