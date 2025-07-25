### 2025-07-24
from random import randint
from functools import reduce

"""
## 통합 실습 - 리마인드 복습

# 부모 클래스
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target):
        damage = randint(5, 15)
        target.hp -= damage
        print(f"{self.name}이(가) {target.name}을 공격! -{damage} 데미지")
    
    def __str__(self):
        return f"{self.name} (HP : {self.hp})"

# 자식 클래스
class Player(Unit):
    def __init__(self, name):
        super().__init__(name, hp=100)

class Monster(Unit):
    def __init__(self, name):
        super().__init__(name, hp=80)

    def attack(self, target):
        damage = randint(8, 20)
        target.hp -= damage
        print(f"{self.name} 몬스터가 {target.name}에게 몬스터 데미지! -{damage} 데미지")

# 인스턴스 생성
units = [
    Player("톡기연하"),
    Player("토마토여나"),
    Monster("슬라임"),
    Monster("고블린")
]

# 유닛 상태 출력
print("\n[초기 유닛 상태]")
for u in units:
    print(u)

# filter로 생존 유닛만
print("\n[HP 50 이상인 유닛만 출력]")
alive = list(filter(lambda u : u.hp >= 50, units))
for u in alive:
    print(u)

# sorted로 HP 순 정렬
print("\n[HP 낮은 순 정렬]")
for u in sorted(units, key = lambda x : x.hp):
    print(u)


# 공격 예시
print("\n[전투 시작!]")
units[0].attack(units[2])
units[2].attack(units[0])
"""

## User 클래스 기반 커뮤니티 시스템
"""
class User:
    def __init__(self, username, login_count, posts, is_banned=False):
        self.username = username
        self.login_count = login_count
        self.is_banned = is_banned
        self.posts = posts

    def write_posts(self):
        self.posts += 1

    def __str__(self):
        return f"{self.username} User Info | 게시글 수 : {self.posts} | 로그인 횟수 : {self.login_count} | 정지 여부 : {self.is_banned}"

class AdminUser(User):
    def __init__(self, username, login_count, posts=0, is_banned=False):
        super().__init__(username, login_count, posts, is_banned)

    def ban_user(self, target_user):
        target_user.is_banned = True

user = [
    User("연하", 5, 20),
    User("도마도", 10, 5),
    User("라떼", 100, 33),
    User("토깽이", 35, 3),
    User("미믹큐", 72, 54),
    AdminUser("운영자", 999)
]

user[5].ban_user(user[2])

normal_user = list(filter(lambda u : not u.is_banned, user))
for u in normal_user:
    print(u)
print()

# 로그인 순
sorted_users = sorted(user, key = lambda u : u.login_count, reverse = True)
for u in sorted_users:
    print(u)
print()

# 포스트 순
sorted_post = sorted(user, key = lambda u : u.posts, reverse = True)
for u in sorted_post:
    print(u)
"""

### 2025-07-25

## Item 클래스 기반 재고/장바구니 시스테

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"상품명 : {self.name} | 가격 : {self.price} | 재고 : {self.stock}"

class Cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, count):
        try:
            if count > item.stock:
                raise ValueError(f"{item.name}의 재고가 부족합니다! (남은 재고: {item.stock})")

            if item.name in self.items:
                self.items[item.name][1] += count
            else:
                self.items[item.name] = [item, count]
            item.stock -= count
        except ValueError as e:
            print(f"[장바구니 오류] {e}")

    def remove_item(self, item_name):
        try:
            removed = self.items.pop(item_name)
            removed[0].stock += removed[1]
        except KeyError:
            print(f"{item_name}은 장바구니에 없습니다!")
        
    def get_total(self):
        return reduce(lambda acc, pair: acc + (pair[0].price * pair[1]), self.items.values(), 0)
    
    def __str__(self):
        result = "=== 장바구니 내용 ===\n"
        for name, (item, count) in self.items.items():
            result += f"{name}: {count}개 (개당 {item.price}원)\n"
        result += f"총액: {self.get_total()}원"
        return result

class DiscountedCart(Cart):
    def __init__(self, discount_rate):
        super().__init__()
        self.discount_rate = discount_rate
    
    def get_total(self):
        return super().get_total() * (1 - self.discount_rate)

pen = Item("펜", 1000, 5)
notebook = Item("노트", 3000, 10)

cart = DiscountedCart(0.1) # 10퍼 할인

cart.add_item(pen, 2)
cart.add_item(notebook, 3)
cart.add_item(pen, 10)
print(cart)