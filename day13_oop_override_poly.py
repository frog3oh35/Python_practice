### 2025-07-23 OOP 오버라이딩, 다형성

## 오버라이딩
"""
# ---
class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name}이 기본 공격을 합니다!")

# 전사 클래스
class Warrior(Character):
    def attack(self):
        print(f"{self.name}가 검으로 공격합니다!")

# 마법사 클래스
class Mage(Character):
    def attack(self):
        print(f"{self.name}가 파이어볼을 날립니다!")

# 객체 생성
c1 = Warrior("토끼전사 연하")
c2 = Mage("마법사 토마토")

c1.attack()
c2.attack()
# ---



## 오버라이딩 + super()
class Character:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name}이(가) 기본 공격을 합니다.")

class Warrior(Character):
    def attack(self):
        super().attack() # 부모의 기본 공격도 실행
        print(f"{self.name}이(가) 검으로 공격합니다!")

class Mage(Character):
    def attack(self):
        print(f"{self.name}이(가) 파이어볼을 날립니다!")


w1 = Warrior("연하")
m1 = Mage("토마토")

w1.attack()
print("----")
m1.attack()

"""

## 

class Character:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name}이(가) 기본 공격을 합니다.")
    
class Warrior(Character):
    def attack(self):
        print(f"{self.name}이(가) 검으로 베었습니당")
    
class Mage(Character):
    def attack(self):
        print(f"{self.name}이(가) 파이어볼을 날립니당")

class Healer(Character):
    def attack(self):
        print(f"{self.name}이(가) 힐을 합니당")

unit1 = Warrior("토끼 전사")
unit2 = Mage("토마토 마법사")
unit3 = Healer("레니니 힐러")

# 유닛 리스트에 넣고 반복문으로 호출 → 다형성!
units = [unit1, unit2, unit3]

for unit in units:
    unit.attack()