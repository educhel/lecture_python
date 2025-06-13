# (1)
# 주문이 들어올 때마다 손님의 이름과 주문 내역이 딕셔너리에 저장됩니다.
# 딕셔너리에서 ‘order’ 값만 출력하세요

order_info = {"customer": "Kim", "order": "iced americano"}
print(order_info['order'])

# (2)
# 배달 주문을 위해, 주소 정보를 추가로 저장해야 합니다
# 아래 딕셔너리에 'address':'Seoul, Jongno-gu'를 추가하고 전체 딕셔너리를 출력하세요.

delivery = {"customer": "Choi"}

delivery['address'] = 'Seoul, Jongno-gu'
print(delivery)

# (3)
# 카페 인기 메뉴의 주문 횟수를 기록한 딕셔너리입니다.
# 모든 메뉴 이름(키)만 리스트로 추출하는 코드를 작성하세요.
orders = {"latte": 21, "americano": 32, "bagel": 15}

print(list(orders.values()))

# 심화
# orders를 가지고, 인기 순위별로 "정렬"하기
order_list = list(orders.items())
print(order_list)

order_list.sort(key=lambda x:-x[1])
print(order_list)

for idx, (menu, cnt) in enumerate(order_list):
    print(f'{idx+1}등')
    print(f'{menu}는 {cnt}개 팔렸습니다.')

# (4)
# VIP 고객인지 확인하려면 'grade'라는 키가 있는지 딕셔너리에서 확인해야 합니다.
# 아래 딕셔너리에 해당 키가 있는지 True/False로 출력하는 코드를 작성하세요.
customer = {"name": "Lee", "point": 1500}

# 방법1
print('grade' in customer)

# 방법2
print(customer.get('grade',False))

# 만약 'grade' 키가 없다면,
# 고객의 'point' 점수를 기준으로 등급을 자동 부여하여 딕셔너리에 추가하세요.
    # - 2000점 이상: "VIP"
    # - 1000점 이상: "Gold"
    # - 500점 이상: "Silver"
    # - 500점 미만: "Bronze"
    
if 'grade' not in customer.keys():
    if customer['point'] >= 2000:
        customer['grade'] = 'VIP'
    elif customer['point'] >= 1000:
        customer['grade'] = 'Gold'
    elif customer['point'] >= 500:
        customer['grade'] = 'Silver'
    else:
        customer['grade'] = 'Bronze'
        
print(customer)