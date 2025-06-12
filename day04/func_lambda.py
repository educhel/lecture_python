# 익명 함수
# lambda
# 왜 이름이 없어? 이름 붙일만큼 중요하지 않아서
# 이름 없어도 된다 -> 굳이 가지고 있지 않아도 되어서

# 기존의 방식
def add(x,y):
    return x+y
result = add(1,4)
print(result)

# 익명함수를 이용한 방식
result = (lambda x,y:x+y)(10,20)
print(result)

number = [1,5,3,5,7]
number_new = sorted(number, key=lambda x:-x)
print(number_new)

print(sorted(number,reverse=True))

# 리스트의 형태
example = [(0, 2), (2, 3), (1, 4), (0, -1)]
new_example = sorted(example,key=lambda x:x[1])
print(new_example)

