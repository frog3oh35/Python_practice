### 2025-07-10 함수와 스코프

## 함수와 스코프
# 함수 안과 밖의 변수는 다르다
# 변수의 유효 범위 (Scope)가 중요하다

def greet():
    message = "안녕!"
    print(message)

greet()
# print(message) > 에러! message는 함수 내부에서만 살아 있음

print()

## 지역 변수Local와 전역 변수Global
x = 10

def func():
    x = 20
    print("함수 안:", x)

func()
print("함수 밖:", x)

print()

## 함수 안에서 전역 변수 사용하기
count = 0

def increment():
    global count
    count += 1

increment()
print("cnt :", count)

print()

## 함수 안에서 함수 안 변수 접근하기

def outer():
    a = "밖"
    def inner():
        print(a)
    inner()

outer()
print()

## practice
x = 5
def add():
    x = 10
    print("함수 안 x:", x)

add()
print("함수 밖 x:", x)