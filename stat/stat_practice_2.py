# 기술 통계의 활용
prices = [300000, 350000, 400000, 450000, 500000, 550000, 600000, 5000000]

print('=== (1) 중앙값의 적용 ===')

print(len(prices)) # 짝수갯수
prices.sort() # 오름차순 정렬

print(f"중앙값 : {(prices[3] + prices[4])/2}") # 짝수 갯수의 중앙값 구하기
# 인덱스 직접 구하지 않고, 계산하여 넣기
# print((prices[len(prices)//2-1] + prices[len(prices)//2])/2)

print(f'평균 : {sum(prices)/len(prices)}')
print('-> 중앙값을 사용해야 하는 이유 : 이상치의 영향을 덜 받기 때문 ')

# 최빈값(mode) 구하기
print("=== (2) 최빈값 구하기 ===")
subjects = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

# 방법 1 - 딕셔너리를 이용하는 방법
subjects_cnt = {}

for subject in subjects:
    if subject not in subjects_cnt.keys():
        subjects_cnt[subject] = 1 # 초기화
    else:
        subjects_cnt[subject] += 1 # 1씩 증가

print(subjects_cnt)

best_sub = ""
best_cnt = 0

for sub, cnt in subjects_cnt.items():
    if cnt > best_cnt:
        best_cnt = cnt
        best_sub = sub

print(f'최빈 과목은 {best_sub}, 나타난 횟수는 {best_cnt}')

# 방법 2 - collections 모듈 사용법
from collections import Counter # 내장 모듈 collections의 Counter 함수
result = Counter(subjects)
print(result.most_common(1))

print("=== (3) 범위와 사분위수 범위 === ")
scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 37, 40, 20, 10, 90]
print(f"범위 : {max(scores) - min(scores)}")

scores.sort()
print(len(scores))
print(scores)
Q2 = scores[len(scores)//2]
Q1 = scores[3]
Q3 = scores[-4]

IQR = Q3 - Q1
print(IQR)

# import numpy as np

# Q1 = np.percentile(scores, 25)
# Q3 = np.percentile(scores, 75)
# print(Q3 - Q1)

print("=== (4) 분산과 표준편차의 이해 ===")

A = [70, 75, 80, 85, 90]
B = [70, 80, 80, 80, 90]

A_mean = sum(A)/len(A)
B_mean = sum(B)/len(B)

# 중심 경향치 (평균) 이 똑같다.
print(f'A의 평균 : {A_mean}')
print(f'B의 평균 : {B_mean}')
print()
A_var = 0

for a in A:
    A_var += (a - A_mean) ** 2
A_var /= len(A)

print(f"A의 분산 : {A_var}")

B_var = 0

for b in B:
    B_var += (b - B_mean) ** 2
B_var /= len(B)

print(f"B의 분산 : {B_var}")
print()


A_std = A_var ** 0.5
B_std = B_var ** 0.5

print(f'A의 표준편차: {round(A_std,3)}')
print(f'B의 표준편차: {round(B_std,3)}')