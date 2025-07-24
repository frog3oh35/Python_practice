### 2025-07-24
from random import randint

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