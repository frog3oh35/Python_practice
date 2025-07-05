### 2025-07-05 조건문 심화 + 딕셔너리 + 함수 입문

## 조건문 심화 - 중첩
age = int(input("나이를 입력하세요: "))
is_student = input("학생입니까? (y/n): ")

if age < 20:
    if is_student == "y":
        print("청소년 학생!")
    else:
        print("청소년이지만 학생은 아님!")
else:
    print("성인!")
print()


## dict 기초
# 딕셔너리란? 키와 값의 쌍으로 이루어진 자료구조
# 리스트는 순서, 딕셔너리는 이름표(키)로 접근
person = {"name": "연하", "age": 27, "city": "Daejeon"}

#값 읽기
print(person["name"])
print(person["age"])
print()

#값 추가/변경
person["job"] = "QA"
print(person)

#값 삭제
del person["city"]
print(person)

print()


## 딕셔너리 반복문
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for name in scores:
    print(name, ":", scores[name])
print()
for name, score in scores.items():
    print(f"{name}의 점수는 {score}점입니다.")
print()

## 함수(def, return) 기본 구조 : 함수 선언과 호출
# 함수 - 코드를 "이름 붙여서 묶어두는 것", 반복 및 재사용이 가능하고 return으로 값을 돌려줌
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("연하")
greet("도마도")
print()

## 함수 : 함수에서 결과값 반홯ㄴ
def add(a, b):
    result = a + b
    return result

sum1 = add(3, 5)
sum2 = add(10, 20)
print("3 + 5 = ", sum1)
print("10 + 20 = ", sum2)