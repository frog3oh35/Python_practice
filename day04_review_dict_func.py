"""

# split Quiz 1. 
print("여러 개의 단어를 입력하세요: ")
words = list(input().split())

print(words)
print()



# 1. func
def say_hello():
    print("안녕 레니니!")

say_hello()


# 매개변수가 있는 함수
def greet(name):
    print("안녕하세요,", name, "님!")

greet("연하")
greet("레니니")
print()

# return이 있는 함수
def add(a, b):
    return a + b

result = add(3, 5)
print("결과: ", result)
print()

# 기본값 있는 함수
def introduce(name="익명", age=0):
    print(f"이름: {name}, 나이: {age}")

introduce()
introduce("연하", 26)
print()

# 2. dictionary
person = {
    "이름": "연하",
    "나이": 27,
    "좋아하는 색": "하늘"
}
print(person)
print()

# dict 값 꺼내기
print("이름:", person["이름"])
print("나이:", person["나이"])
print()

# 값 추가
person["취미"] = "코딩...이고 싶음"
print(person)
print()

# 값 수정
person["이름"] = "요나"
print(person)
print()

# key, value 확인
print("키 목록:", person.keys())
print("값 목록:", person.values())
print()

# 키 삭제
del person["나이"]
print(person)




# basic Quiz 1
def print_heart():
    print("❤️❤️❤️ 나는 내가 조아 ❤️❤️❤️")

print_heart()
print()

# 입력 매개변수 버전
def print_heart(message):
    print(f"❤️❤️❤️ {message} ❤️❤️❤️")

message = input("메세지를 입력해보세요: ")
print_heart(message)
print()


# basic Quiz 2
def greet_person(name):
    print(f"안녕하세요, {name}님!")

name = input("이름을 입력하세요: ")
greet_person(name)
print()


# basic Quiz 3
def add_numbers(a, b):
    return a + b

## add
a, b = map(int, input("두 수를 입력하세요: ").split())
result = add_numbers(a, b)

print("결과:", result)
print()

"""

# dictionary basic Quiz 1
amI = {
    "이름" : "연하",
    "MBTI" : "ISFJ",
    "사는 곳" : "대전"
}

print(amI)
print()

# changing Value
amI["MBTI"] = "ISTJ"
print(amI)

# DELETE Value
del amI["사는 곳"]

print("키 목록:", amI.keys())
print("값 목록:", amI.values())