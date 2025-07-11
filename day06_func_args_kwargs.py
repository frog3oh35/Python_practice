### 2025-07-11
### 가변 인자 *args **kwargs 실습

# 위치 인자 (Positional Arguments) : 순서대로 값을 넣는 방식
# 함수에서 정의한 매개변수 순서에 맞게 차례대로 값이 들어감

# 키워드 인자 (Keyword Arguments) : 이름을 붙여서 매개변수명=값 형태로 전달하는 방식
# 순서 상관없이 어떤 매개변수에 어떤 값을 줄지 명시

## *args 위치 기반 가변 인자
# *args는 몇 개의 인자가 들어올지 모를 때 사용해요
# 함수 안에서는 튜플(tuple)로 전달됩니다
def greet_all(*names):
    for name in names:
        print(f"안녕, {name}!")

greet_all("연하", "정훈", "커비")
print()

## **kwargs 키워드 기반 가변 인자
# **kwargs는 키 = 값 형태의 인자를 여러 개 받을 때 사용해요
# 함수 안에서는 딕셔너리로 전달
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_user_info(name="연하", age = 27, mbti = "ISFJ")
print()

# *args와 **kwargs 함께 쓰기
def mixed_function(*args, **kwargs):
    print("위치 인자:", args)
    print("키워드 인자:", kwargs)

mixed_function("연하", "커비", age=27, hobby="coding")
print()

# 추가 예제
def report(title, *items, **details):
    print(f"📜 {title}")
    print("항목:")
    for item in items:
        print(f" - {item}")
    print("세부정보:")
    for key, value in details.items():
        print(f" {key}: {value}")

report(
    "연하의 Daily Report",
    "Python 공부", "애슐리 뺑이치기", "정처기 공부",
    mood="productive",
    hours=5,
    location="Home and Ashley"
)
print()

# 추가 예제2
def check_attendance(date, *names, **status):
    print(f"출석 날짜: {date}")
    print()
    print("출석 대상자 명단:")
    for name in names:
        print(f"- {name}")
    
    print()
    print("출석 상태:")
    for person, status in status.items():
        print(f"{person}: {status}")

check_attendance(
    "2025-07-12",
    "연하", "레니니", "수정",
    연하 = "출석", 레니니="지각", 수정="결석"
)
