### 2025-07-22 OOP 기초 복습 및 객체지향의 핵심 원칙 정리
### 캡슐화, 독립성, str() 커스터마이징


# OOP 기초 복습
"""
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}의 체력이 {amount}만큼 회복되어 현재 체력은 {self.hp}입니다.")

    def attack(self, other):
        print(f"{self.name}가(이) {other.name}을 공격합니다!")
        other.hp -= 10
        print(f"{other.name}의 체력이 {other.hp}가 되었습니다.")
    
c1 = Character("연하", 80)
c2 = Character("도마도", 100)

c1.heal(20)
c1.attack(c2)
"""

## 캡슐화 : BankAccount 클래스
# 기능 요구 사항 : 이름/계좌번호/잔액, 입금 메서드, 출금 메서드, 현재 잔액 보기, __str__()로 예쁘게 출력
class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0 # 외부에서 접근 불가 (캡슐화)

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}원 입금되었습니다. 현재 잔액: {self.__balance}원")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액 부족!")
        else:
            self.__balance -= amount
            print(f"{amount}원 출금되었습니다. 현재 잔액 : {self.__balance}원")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"계좌 정보 {self.owner} / {self.account_number} / 잔액 : {self.__balance}원"

acc1 = BankAccount("연하", "123-343")
acc1.deposit(50000)
acc1.withdraw(20000)
print(acc1)
print()


## 독립성 : Book 클래스
# 기능 요구 사항 : 책 제목, 작가, 가격을 속성으록 가짐

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount
        print(f"{percent}% 할인 적용! 새로운 가격: {int(self.price)}원")
    
    def __str__(self):
        return f"『{self.title}』 - {self.author} / {int(self.price)}원"

b1 = Book("토끼의 모험", "연하", 15000)
b2 = Book("늑대의 전략", "정훈", 18000)

print(b1)
print(b2)

b1.apply_discount(20)
print(b1)
print(b2)
print()

## 캡슐화 + 독립성 + str 커스터마이징 복습

class RPG:
    def __init__(self, name, job, hp=100, power=10):
        self.name = name
        self.job = job
        self.__hp = hp
        self.power = power
    
    def attack(self, other):
        print(f"{self.name}의 공격! {other.name}이 데미지를 받습니다.")
        other.take_damage(self.power) # 직접 깎지 말고 요청만 함
    
    def take_damage(self, amount):
        self.__hp -= amount
        print(f"{self.name}의 hp가 {self.__hp}이 되었습니다.")

    def __str__(self):
        return f"{self.job} {self.name} (HP : {self.__hp}), 공격력 : {self.power})"

c1 = RPG("연하", "QA", 300, 20)
c2 = RPG("정훈", "무역왕", 300, 50)

print(c1)
print(c2)
c1.attack(c2)
print(c2)