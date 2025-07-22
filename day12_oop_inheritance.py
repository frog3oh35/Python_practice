### 2025-07-22 OOP 상속

## 부모 클래스 Character
class Character:
    def __init__(self, name, job, hp, power):
        self.name = name
        self.job = job
        self.hp = hp
        self.power = power

    def attack(self, other):
        print(f"{self.name}이(가) {other.name}을 공격합니다!")
        other.hp -= self.power
        print(f"{other.name}의 체력이 {other.hp}가 되었습니다.")

    def __str__(self):
        return f"{self.job} {self.name} (HP : {self.hp}, Power : {self.power})"

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "전사", 120, 15)
    
class Mage(Character):
    def __init__(self, name):
        super().__init__(name , "마법사", 80, 25)

w1 = Warrior("연하")
m1 = Mage("도마도")

print(w1)
print(m1)

w1.attack(m1)
print(m1)