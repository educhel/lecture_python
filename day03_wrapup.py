# 전체복습

print('===변수===')
# 문자열을 담은 변수 hello
# 코드는 위에서 아래로 실행이 되기 때문에
# 사용하기 위해선 "먼저" 정의,할당 필요!

# hello 라는 변수에 인삿말(문자열)을 할당
# 할당 연산자 = 가 쓰임
hello = '오늘도 좋은 아침입니다!'
print(hello) # 먼저 정의되거나 할당되지 않으면 사용할 수 없다!
print(id(hello))

# 재할당
hello = '봉주르!'
print(hello)
print(id(hello))

# hello = '오늘도 좋은 아침입니다!'

print('===입력과 출력===')
# 사용자 - 컴퓨터가 접점이 필요
# 나한테 직접 보여줘! -> 'print'
# 내가 너한테 값을 줄게 -> 'input'
# input 함수로 입력받은 모든 자료형은 "문자열"

# name = input('이름을 입력해 주세요.: ') 
# print(f'안녕하세요, {name}님')
# print()

# students = input('출석 목록:') 
# 문자열로 들어온 값을 '처리'를 해줘야 할 수 있다.
# students = students.split(' ')
# print(type(students))
# print(students)

word1 = '오늘은'
word2 = '목요일'
word3 = '주말까지'
word4 = '단 2일!'

# , 를 통해 한 번에 출력 가능
print(word1, word2, word3, word4) 
# 문자열 끼리의 + 연산을 통해서도 연결 가능
print(word1 + word2 + word3 + word4)

# print 함수의 파라미터를 조절하면서 원하는 형식으로 출력 가능하다.
print(word1, word2, word3, word4, sep='~') 
print(word1, word2, word3, word4, sep='!!!!')

# end 
print(word1,end=' ')
print(word2,end=' ')
print(word3,end=' ')
print(word4)

print('===연산자===')
# 연산 -> 처리
# 1. 산술연산자
a = 10
b = 2

print(a * b) # 사칙연산 +, -, *, /
print(a // b) # 몫
print(a % b)  # 나머지
print(a ** 0.5) # 제곱

# 2. 복합연산자
# 주의! 
# 복합 연산은 "기존에 있던 변수"에 어떠한 계산을 거쳐서 
# 재할당하는 것을 의미합니다.

c = 0 # 이미 정의 완료한 변수여야 한다.
c += 1
print(c)

d = '' # 문자열도 + 연산이 가능하기 때문에
d += '플러스!'
d += '플러스!'

print(d)

# 3. 비교연산자
# 두 값을 비교 -> 참과 거짓을 판단
# 대소비교 : >, <, >=, <=
# 일치비교 : ==, !=

answer = 'a' == 1 # 일치비교
# answer = 'a' > 1 # 대소비교
print(answer) # True, False

# 4. 논리연산자
print(a, b)
answer = a == 1 and b > 10
print(answer)

# +) 멤버십 연산자
