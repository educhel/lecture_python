# 커피 구매와 거스름돈 계산 프로그램
money = int(input('얼마 있어요? : ')) # int 형변환
print(type(money))

price = 2000
# 구매 가능한 커피 잔수 - 몫
cnt = money // price 
print(cnt)

# 거스름돈
# 방법 1
# 나머지 (%)
change = money % price
print(change)

# 방법 2
# 결제한 금액 빼기
change = money - (cnt * price)
print(change)