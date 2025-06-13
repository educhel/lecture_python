# 카운트 다운이 있는 로또 번호 추첨기 만들기
import random
import time

for i in range(5):
    print(f'{5-i}초 남았습니다.')
    time.sleep(1)

lotto = list(random.sample(range(1,46),6))
lotto.sort() 
print(lotto)