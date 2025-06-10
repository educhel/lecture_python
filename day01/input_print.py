print('======입력=======')
# 사용자 입력

# input을 통해서, 사용자에게 입력 받습니다.
# 자료형은 항상 str입니다. -> 다른 자료형으로 바꾸고 싶을때? 명시적 형변환
# 사용자 입력받은 값을 숫자로 변환하고 싶다면?

# name = input('이름을 입력해 주세요.:')
# age = int(input('나이를 입력해 주세요.:'))

# print(f'안녕하세요, {age+1}살의 {name}님!')

# print(type(name))
# print(type(age))

print('======출력=======')
# 터미널 상에 출력(보여주기) 위함이다.
word1 = 'hello'
word2 = 'python'
word3 = 'yeah'

# 콤마(,)를 이용하여, 여러 개의 값을 출력할 수 있다.
# 공백(기본값 = 공백)을 기준으로 연결되어 한줄에 출력된다.
print(word1, word2, word3)
print(word1, word2, word3, sep='!') # 연결되는 공백을 !으로 바꿀 수도 있다.
print(word1, word2, word3, sep='!',end='!')

print(word1,end='!')
print(word2)

# 입력 = input() -> 터미널에서 받는다.
# 출력 = print() -> 터미널에 출력된다.