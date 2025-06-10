# 연습문제 해설
height = float(input("키를 입력해 주세요 (단위 :m) "))
weight = float(input("몸무게를 입력해 주세요 (단위 :kg) "))

print(weight, height)
print(type(weight), type(height))
# <class 'float'> <class 'float'>

# BMI 계산식
bmi = weight / (height * height)
print(bmi)

# 조건문
if bmi >= 25:
    print('비만')
elif bmi >= 23:
    print('과체중')
elif bmi >= 18.5:
    print('정상')
else:
    print('저체중')