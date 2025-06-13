# (1)
# 카페에서 판매 중인 음료 메뉴가 아래와 같이 리스트로 저장되어 있습니다.
# 어느 날, "딸기라떼"가 신메뉴로 출시되어, 'americano' 뒤에 추가해야 합니다.
menu = ["americano", "latte", "cappuccino"]
print(type(menu))

# 리스트의 특징 - 가변 자료형
# menu.append('strawberry latte') # 맨 뒤에 추가하는 경우
# americano 뒤에 추가하려면?
menu.insert(1,'strawberry latte')
print(menu)


# (2)
# 어느 손님이 “오늘 라떼는 빼주세요”라고 요청했습니다.
# 1 - 메뉴에서 'latte'를 삭제한 뒤, 
# 2 - 삭제한 메뉴가 실제로 삭제되었는지 True/False로 확인하는 코드를 작성하세요.

menu.pop(menu.index('latte')) # 위치를 기준으로도 가능하다.
# 위치를 기준으로 삭제하기 때문에 또 한번 우리가 'latte'의 위치를 확인해야 합니다.
# menu.remove('latte')
print(menu)
print('latte' not in menu) # 멤버십 연산을 통해서 확인

# (3)
# 오늘 아침 재고 조사를 했더니, 기존 메뉴에 빵 리스트가 따로 있다는 사실을 알게 되었습니다.
# 음료 리스트와 빵 리스트를 합쳐, 하나의 ‘통합 메뉴판’ 리스트로 만드세요.
bread = ["bagel", "croissant", "scone"]

# menu.extend(bread)
# print(menu)

total_menu = menu + bread # 새로운 리스트 만들기
print(total_menu)

# (4)
# 카페 점주님이 메뉴의 가나다순 정렬을 원하십니다.
# 통합 메뉴판을 오름차순으로 정렬하는 코드를 작성하세요.

# 방법 1
# total_menu.sort()
# print(total_menu)

# 방법 2
total_menu = sorted(total_menu)
print(total_menu)