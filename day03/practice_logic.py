# 떡잎마을 반장선거
# 후보가 없는 반장선거

votes = ['짱구','짱구','수지','짱구','훈이','맹구',
        '수지','수지','수지','짱구','유리','철수','수지']
result = {} # 딕셔너리

# 누가 반장이 되었을까요?
for vote in votes:
    if vote not in result:
        result[vote] = 1
    else:
        result[vote] += 1

print(result)
print('수지가 반장이 되었습니다.')

# 이후 배울 내용 맛보기
result_lst = list(result.items())
print(result_lst)
result_lst.sort(key=lambda x:-x[1])
print(result_lst)
print(result_lst[0][0])