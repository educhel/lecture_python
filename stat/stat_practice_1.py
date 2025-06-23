# 컨테이너 자료형
scores = [85, 90, 78, 95, 88]

print(scores)

print("=== 1. 평균 구하기 ===")
print(sum(scores)/len(scores)) # 87.2

print("=== 2. 중앙값 구하기 ===")
# 리스트를 정렬하는 방법
# 내장함수 sorted -> 정렬이 완료된 새 리스트를 반환
# 리스트 메서드 .sort() -> 기존의 리스트를 변경

scores.sort()
print(scores[2])

# 최빈값
print("=== 3. 최빈값 구하기 ===")
score_cnt = {}

for score in scores:
    if score not in score_cnt:
        score_cnt[score] = 1
    else:
        score_cnt[score] += 1

print(score_cnt)
print("최빈값은 구할 수 없음")

print("=== 4. 범위 구하기 ===")
score_range = max(scores) - min(scores)
print(score_range)

print(scores[-1]-scores[0])