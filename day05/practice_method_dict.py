# (1)
# 주문이 들어올 때마다 손님의 이름과 주문 내역이 딕셔너리에 저장됩니다.
# 딕셔너리에서 ‘order’ 값만 출력하세요

order_info = {"customer": "Kim", "order": "iced americano"}

# (2)
# 배달 주문을 위해, 주소 정보를 추가로 저장해야 합니다
# 아래 딕셔너리에 'address':'Seoul, Jongno-gu'를 추가하고 전체 딕셔너리를 출력하세요.

delivery = {"customer": "Choi"}

# (3)
# 카페 인기 메뉴의 주문 횟수를 기록한 딕셔너리입니다.
# 모든 메뉴 이름(키)만 리스트로 추출하는 코드를 작성하세요.
orders = {"latte": 21, "americano": 32, "bagel": 15}

# (4)
# VIP 고객인지 확인하려면 'grade'라는 키가 있는지 딕셔너리에서 확인해야 합니다.
# 아래 딕셔너리에 해당 키가 있는지 True/False로 출력하는 코드를 작성하세요.
customer = {"name": "Lee", "point": 1500}

# 만약 'grade' 키가 없다면,
# 고객의 'point' 점수를 기준으로 등급을 자동 부여하여 딕셔너리에 추가하세요.
    # - 2000점 이상: "VIP"
    # - 1000점 이상: "Gold"
    # - 500점 이상: "Silver"
    # - 500점 미만: "Bronze"

