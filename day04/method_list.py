# 리스트 메서드 

numbers = [10,20,30,40,50]
print(numbers)

# 추가
# 가장 마지막 위치에 새로운 원소 (딱 하나만) 추가
numbers.append(60)
print(numbers)
print(type(numbers))
print(id(numbers))

# numbers.append([10,20,30,40])
# print(numbers)

# 여러 개 추가하고 싶으면?
# 다른 메서드 사용 -> 가변 자료형
numbers.extend([10,20,30,40])
print(numbers)
print(id(numbers))

# numbers = numbers+[10,20,30,40]
# print(id(numbers))

# 삭제 - 위치(인덱스)를 기준으로 삭제
deleted_value = numbers.pop(1)

print(numbers)
print(deleted_value)

# 삽입
numbers.insert(3,1000)
print(numbers)

# 특정한 원소
# 삭제 - 원소의 값을 기준으로 삭제
numbers.remove(10)
print(numbers)

# 값을 센다.
# -> 값을 기준으로 몇개인지 세기 때문에 "리스트"를 바꾸지 않습니다.
cnt = numbers.count(1000000000)
print(cnt)

# 원소 값을 기준으로 위치를 찾을 수도 있다!
idx = numbers.index(40)
print(idx)
print(numbers[idx])

# 내장함수 soted() : 정렬하여 새로운 리스트를 반환한다.
# 메서드 sort() : 기존의 리스트를 정렬한다.
numbers.sort(key=lambda x:x%3)
print(numbers)

# 순서를 뒤집어 버린다.
print(numbers[::-1])
numbers.reverse()
print(numbers)