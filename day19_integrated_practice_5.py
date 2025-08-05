### 2025-08-05 
## 객체지향 + 통합 문법 연습 6일차 될 때까지 반복 연습 간다!!!

class Developer:
    def __init__(self, name, experience, stack, remote):
        self.name = name
        self.experience = experience
        self.stack = stack
        self.remote = remote

    """
    name: str
    experience: int
    stack: List[str]
    remote: bool
    """

    def has_skill(self, skill):
        return skill in self.stack

    def is_remote_ok(self):
        return self.remote
    
    def __str__(self):
        return f"{self.name} : [{', '.join(self.stack)}] : 경력 {self.experience}년 : 원격여부 {self.remote}"
    
    def __repr__(self):
        return self.__str__()

dev = [
    Developer("연하", 1, ["Python", "Cypress", "Postman", "JavaScript"], True),
    Developer("정렬", 5, ["JavaScript", "TypeScript", "Firebase", "AWS"], False),
    Developer("나무", 3, ["Python", "Java", "Tensorflow", "Keras"], True),
    Developer("출력", 8, ["Python", "JavaScript", "Spring", "React", "AWS", "Jenkins"], True),
    Developer("진수", 7, ["Python", "JavaScript", "Go", "Linux", "Docker", "Jenkins"], False)
]
"""
# 기술 스택 포함 확인
print(dev[0].has_skill("Java"))
print(dev[2].has_skill("Tensorflow"))
print()

# 원격 ok?
print(dev[2].is_remote_ok())
print()


# con_1 : 특정 기술 보유자 filter
print("✨   JS 가능 Dev")
JS_devs = list(filter(lambda d : d.has_skill("JavaScript"), dev))

for d in JS_devs:
    print(d.name, ":", d.stack)
print()

# con_2 : 경력 정렬
print("❤️   Dev 경력 기준 정렬")
for d in sorted(dev, key = lambda d : d.experience, reverse = True):
    print(f"Dev {d.name} - {d.experience}년")
print()

# con_3 : 원격 가능 + 특정 기술 보유자
print("🐰   원격 가능 + Jenkins 가능 Dev")
satisfy_con = list(filter(lambda d : d.has_skill("Jenkins") and d.is_remote_ok(), dev))

for d in satisfy_con:
    print(f"{d.name} / {d.stack}")
print()

# con_4 : 스택 개수 기준 필터
print("🐍   기술 스택 6개 이상 가능 Dev")
stack_six = list(filter(lambda d : len(d.stack) >= 6, dev))
for d in stack_six:
    print(f"{d.name} / {d.stack}")
print()

# con_5 : 특정 기술 조합 보유 - 복습 필요
print("🍳   Py + Docker 가능 Dev")
target_skills = ["Python", "Docker"]

match_all = list(filter(lambda d: all(skill in d.stack for skill in target_skills), dev))
for d in match_all:
    print(d)
print()

# con_6 : 특정 경력 내 filter
print("🗓️   Junior Dev (3~5년차)")
junior_dev = list(filter(lambda d : 3 <= d.experience <= 5, dev))
for d in junior_dev:
    print(f"{d.name}, 경력 {d.experience}년")
print()
"""

# console
while True:
    print("\n🖥️   Dev filtering System")
    print("1. 특정 기술 보유자 조회")
    print("2. 경력별 분류")
    print("3. 기술 조합 검색")
    print("4. 종료")
    choice = input("번호를 입력하세요: ")

    if choice == "1":
        skill = input("찾고 싶은 기술 입력: ").strip()
        result = list(filter(lambda d: d.has_skill(skill), dev))
        print(f"\n🔍   [{skill}] 기술 보유자")
        for d in result:
            print(f"- {d.name} / {', '.join(d.stack)}")

    elif choice == "2":
        print("\n🗓️     경력 분류: ")
        print("1. 신입 (0~2년)")
        print("2. 주니어 (3~5년)")
        print("3. 시니어 (6년 이상)")
        sub = input("번호 선택: ")

        if sub == "1":
            result = list(filter(lambda d: d.experience <= 2, dev))
        elif sub == "2":
            result = list(filter(lambda d: 3 <= d.experience <= 5, dev))
        elif sub == "3":
            result = list(filter(lambda d: d.experience >= 6, dev))
        else:
            print("잘못된 입력입니다.")
            continue

        print("\n📚     결과:")
        for d in result:
            print(f"- {d.name} ({d.experience}년)")

    elif choice == "3":
        input_skills = input("찾을 기술들을 콤마로 구분해 입력하세요 (ex: Python, Docker): ")
        target_skills = [s.strip() for s in input_skills.split(",")]
        result = list(filter(lambda d: all(skill in d.stack for skill in target_skills), dev))

        print(f"\n✅  모든 기술 [{', '.join(target_skills)}] 보유자:")
        for d in result:
                print(f"- {d.name} / {d.stack}")

    elif choice == "4":
        print("🖐️  프로그램 종료!")
        break

    else:
        print("유효하지 않은 입력입니다.")