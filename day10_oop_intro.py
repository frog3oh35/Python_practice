### 2025-07-17 객체지향

## class - 붕어빵 틀
## instance - 붕어빵 틀로 만든 붕어빵 그 잡채

## __init__ : 생성자 메서드
## self : 자기 자신 인스턴스를 가리키는 키워드 (C#에서의 this와 비슷한 개념)

"""
# Person 클래스
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("안녕! 나는", self.name)

p = Person("연하")

p.say_hello()

# Animal 클래스 
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(f"{self.name}가 {self.sound} 하고 울어요!")

dog = Animal("강아지", "멍멍")
cat = Animal("고양이", "야옹")

dog.speak()
cat.speak()

"""


## Part 2.
"""
# 메서드에서 속성 변경하기 - 캐릭터 클래스

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}의 체력이 {amount}만큼 회복되어 현재 체력은 {self.hp}입니다.")
    
    def attack(self, other):
        print(f"{self.name}이(가) {other.name}을(를) 공격합니다!")
        other.hp -= 10
        print(f"{other.name}의 체력이 {other.hp}가 되었습니다.")

c1 = Character("연하", 90)
c1.heal(20)

c2 = Character("정훈", 100)
c1.attack(c2)
# other도 self 처럼 인스턴스이며, 객체 간 상호작용이 가능해진다
"""

# 예제 : 계산기 클래스

class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, number):
        self.total += number
        print(f"현재 합: {self.total}")
    
    def reset(self):
        self.total = 0
        print("초기화 되었습니다.")

calc = Calculator()
calc.add(5)
calc.add(10)
calc.reset()


# 예제 : 학생 클래스

class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def study(self):
        self.score += 10
        print(f"{self.name}의 점수가 {self.score}점이 되었습니다.")

s1 = Student("여나추")
s2 = Student("오빠추")

s1.study()
s2.study()