print('===리스트 답안===')
# 1. a 라는 리스트 선언한다. 이때, 값은 1,2,4,5,8을 순서대로 넣는다.
# 2. a 라는 리스트 가장 마지막 위치에 10을 추가한다.
# 3. a 의 가장 첫 번째 위치의 값을 삭제한다.
# 4. 각 과정을 거치며 a 의 주소값을 확인한다.

# 리스트의 특징 -> 순서가 있고, 가변 자료형
a = [1,2,4,5,8]
print(a)
print(id(a))

# 값 추가
a.append(10)
print(a)
print(id(a))

# 값 삭제
a.pop(0)
print(a)
print(id(a))

## 문자열
# 1. 알파벳 소문자가 붙어 있는 문자열을 입력으로 받아,
# 각 글자를 원소로 갖는 리스트로 변환하여 출력하세요.
print('====형변환====')
word = input('단어를 입력해 주세요.')
print(word)
print(type(word))
print(id(word))

# 리스트로 변환하여 재할당
word = list(word)
print(word)
print(type(word))
print(id(word))

# 2. 문자열을 입력받아, 해당 문자열이 펠린드롬인지 아닌지 판별하세요. 
# 앞으로 읽은 것과 거꾸로 읽은 것이 같은 단어를 펠린드롬이라고 합니다.
word = input('단어를 입력해 주세요.')

# 문자열 슬라이싱
print(word[::-1])
print(word == word[::-1])

if word == word[::-1]:
    print('펠린드롬입니다.')
else:
    print('펠린드롬이 아닙니다.')