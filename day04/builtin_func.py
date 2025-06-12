# 내장함수
numbers = [1,4,6,10,44,-6,-8]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(abs(numbers[-1]))
print()

# 순서가 있는 컨테이너 
# 순서가 있다는 것은 "정렬"되었다는 것은 아니다!
print(numbers)
print(id(numbers))

numbers_new = sorted(numbers)
print(numbers_new)
print(id(numbers_new))
print(numbers)
print(id(numbers))

number_str = list(map(str,numbers))
print(number_str)