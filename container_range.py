# range
# 연속된 정수 목록

# range 특징 1 : 순서가 있는 정수 목록
# 인덱싱 하여 볼 수 있다.
number = range(1,11)
print(number[1])
print(number[1:3])
print(list(number)) 

# range 특징 2 : 불변 자료형
# number[1] = 1
# 변경할 수 없다!

# 주요 사용법
for i in range(1,11,2):
    print(i)