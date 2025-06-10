# 컨테이너 특성
# 순서 o, x
# 변경 o, x

# 형 변환
# 문자열 -> 리스트
# 각 문자가 개별 원소로 바뀌고, "순서o","변경o"
word = 'python'
word_lst = list(word)
print(word_lst)

# range -> 리스트
number_range = range(10)
number_lst = list(number_range)

print(number_range)
print(number_lst)

# str, tuple -> 할 순 있지만 사용하는데 신경 써야 한다.
str_number = str(number_lst)
print(str_number)
print(str_number[3]) # 공백조차 문자열이 되어 버림!