# 내장함수 len 구현하기
# 사용자 정의 함수
# len_func -> "길이"를 확인할 수 있는 함수 만들기

numbers = [1,2,3,4,5,6,7]
print(numbers)
answer = len(numbers)
print(answer)

# 선언 (define)
def len_func(container):
    # 여러 개의 값이 존재하는 입력
    size = 0 # 세기 위한 변수 생성
    for i in container:
        size += 1
    return size

# 호출 (call)
answer = len_func(numbers)
print(answer)