# 반복문 - while
# while True: # 현재는 무한하게 반복 
#     print('영원히 반복...')

# while 조건:
    # 반복되는 코드
    
numbers = [1,2,3,4,5]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1 # 조건을 변화시킬 수 있는 식이 꼭 필요하다

# while 문으로 1부터 10까지 출력하기
for i in range(1,11):
    print(i)

i = 1
while i < 11: # 증감식에서 꼭! 조건을 변화 시킬 수 있어야 한다.
    print(i)
    i += 1 # 중요한 증감식 부분!

# 간단 실습
# while문으로 1부터 10까지 더한 값 55를 출력하기
print('=== 간단 실습 ===')
n = 1
answer = 0

while n <= 10:
    answer += n # 재할당 +=
    n += 1      # 조건에 대한 증감식

print(answer)