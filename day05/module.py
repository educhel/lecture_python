# 기초 내장 모듈

print("===random===")
# 무작위로 무언가를 뽑을 때, 사용하는 모듈
import random

# 랜덤 숫자 뽑기
num = random.randint(1, 5) # 1 ~ 5 사이의 정수값을 랜덤하게 뽑기
print(num)

# 랜덤한 목록 중에 하나 뽑기
candidates = ['민지님','나라님','경현님']
a = random.choice(candidates)
print(a)

candidates.extend(['혜지님','정원님','한별님','유정님'])

# 원하는 갯수만큼 샘플 뽑기
samples = random.sample(candidates,3)
print(samples)

# 무작위 섞기
random.shuffle(candidates)
print(candidates)

# 랜덤을 이용해서 할 수 있는 것들!
# 1. 로또 추첨기
# 2. 발표자 뽑기
# 3. 식사조 뽑기

# time 모듈
# 시간을 다루는 모듈
print('===time모듈===')
import time

# time.sleep 함수
print('한숨 자겠습니다.')
for i in range(5):
    time.sleep(1)
    print(f'1초 기다린 후, {i} 출력')
print('일어났다!')

# 로또 추첨 / 팀배정 -> 두구두구 "카운트다운"
