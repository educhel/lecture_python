# 객체지향 프로그래밍

class Student: # 학생설계
    status = '피곤함'
    population = 0
    
    def __init__(self, name, weight):
        self.name = name
        self.status = Student.status
        self.weight = weight
        self.level = 0
        Student.population += 1
    
    def study(self):
        self.level += 1
        
    def introduce(self):
        print(f'저는 {self.name}, 학생이죠.')
        
    def eat(self, menu):
        if menu == '오므라이스':
            self.weight += 0.5
        elif menu == '부대찌개':
            self.weight += 1.5
        else:
            self.weight += 1
    
    def run(self):
        self.weight -= 1

student1 = Student('짱구',10)
# print(Student.population)
print(student1.level)

student1.study()
student1.study()
student1.study()

print(student1.level)
print(student1.status)

student1.eat('오므라이스')
print(student1.weight)

student1.run()
print(student1.weight)