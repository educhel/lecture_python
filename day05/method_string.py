# 문자열
# 특징 1 : 순서가 있다.
# 특징 2 : 변경 불가능 -> 불변 자료형 (immutable)

# 문자열 분할
# 특정한 구분자를 기준으로 나눌 수 있다.
sentence = "hello@python@!"
sentence_list = sentence.split('@') # 자기자신을 바꾸지 않고, 반환
print(sentence_list)

# 언제 사용하는가?
# 코딩테스트와 같을 때 자주 사용
# students = input('학생이름을 입력해주세요.').split()
# print(students)
# print(type(students))

# 문자열을 원소로 가지는 컨테이너의 각 값을
# 구분자를 기준으로 이어 붙이기 
# -> 새로운 문자열을 반환
# answer = "~".join(students)
# print(answer)

string_list = ["There", "are", 2, "people", "."]  # 중간에 정수가 섞여있음
string_list = list(map(str,string_list))

print(" ".join(string_list))

# 문자열 처리
word = '        오늘 하루도 힘내 봅시다~         '
print(len(word))

# 문자열은 불변 자료형 이기 때문에 그자체를 바꾸진 못하고,
# 새로운 문자열을 반환한다.
clean_word = word.strip()
print(clean_word)

# 문자열
# 특정문자의 위치를 확인하는 메서드
idx = clean_word.index('힘')
print(idx)
print(clean_word[idx])

idx = clean_word.find('짠')
print(idx)

# 원하는 값으로 대체하는 메서드
# 문자열 불변 -> 반환
new_word = clean_word.replace(' ','')
print(new_word)
