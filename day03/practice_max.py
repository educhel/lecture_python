# 실전 문제풀이
# max, min
print('====최댓값 찾기====')

numbers = [190, 49, 598, 2, 50, -1]
max_value = -999 # 충분히 작은 최댓값

# numbers를 반복하며, 각 요소와 max_value 비교
# 비교한게 더 큰 값을 다시 max_value에 할당
for num in numbers:
    if max_value < num:
        max_value = num
    else:
        pass

print(max_value)

print('====최솟값 찾기====')
numbers = [190, 49, 598, 2, 50, -1]
min_value = 999 # 충분히 큰 최소값

for num in numbers:
    # print(min_value)
    # 모르겠으면, 반복문을 돌며 print 찍어서 확인하라!
    if min_value > num:
        min_value = num

print(min_value)