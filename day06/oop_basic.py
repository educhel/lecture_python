# 객체지향프로그래밍 (oop)
# 파이썬에서 모든 것은 "객체"다!

# 객체는 정보(속성)를 가지고 있고,
# 객체는 행동(메서드)을 할 수 있다.

# 객체를 만들기 위해 class 라는 설계도를 만든다.

class Person:
    species = '호모 사피엔스'
    
    def __init__(self, name, init_age): 
        # 인스턴스 만들때 꼭 넣어줘야 함
        self.name = name
        self.age = init_age
    
    def introduce(self):
        print(f'안녕하세요, 저는 {self.name}입니다.')
    
    def birthday(self):
        self.age += 1

student = Person('alex',3)
print(student.age) # 정보(속성)
student.introduce() # 행동(메서드)
student.birthday()
student.birthday()
print(student.age)
print(student.species) # 모든 인스턴스가 공유하는 속성