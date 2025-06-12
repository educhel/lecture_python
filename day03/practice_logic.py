# 떡잎마을 반장선거
# 후보가 없는 반장선거

votes = ['짱구','짱구','수지','짱구','훈이','맹구',
        '수지','수지','수지','짱구','유리','철수','수지']
result = {} # 딕셔너리

# 누가 반장이 되었을까요?
# 투표 내역을 하나하나 돌아가며, 값을 센다.
    # 1) 해당 후보자가 표를 "득표"했을 때
    # 2) 표 내역에서 후보자의 이름이 나왔을 때,
        # 1) 만일 후보자 등록이 완료되었다면 +1
        # 2) 만일 후보자 등록이 되어 있지 않다면? 등록 후에 1을 할당

# result['짱구'] = 1 # 생성 가능
# result['짱구'] += 1 # 복합 연산
# result['짱구'] = result['짱구'] + 1

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
# result_lst.sort(key=lambda x:-x[1])
result_lst = sorted(result_lst,key=lambda x:-x[1])
print(result_lst)
print(result_lst[0][0])