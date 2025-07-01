# Day 1 : Python 기초

# 1. 변수 선언
name = "연하"
age = 27
print("이름: ", name)
print("나이: ", age)
print()

# 2. 조건문
age = 18
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")
print()

# 3. 불린 변수 예시
is_hungry = True
if is_hungry:
    print("배고파욧")
print()

# 4. 비교연산자 / 논리연산자
x = 10
y = 5
print(x > y)
print(x == y)
print(x !=y and y <10)
print()

# 5. 문자열 더하기 & 곱하기
name = "여나"
greeting = "안녕 " + name + "!"
print(greeting)

print("🐍" * 5)
print()

# 6. 숫자 연산
a = 10
b = 3
print("덧셈: ", a + b)
print("뺄셈: ", a - b)
print("곱: ", a * b)
print("나눗셈: ", a / b)
print("몫: ", a // b)
print("나머지: ", a % b)
print("거듭제곱: ", a ** b)

print()

# 7. 변수 교환 (swap)
x = 100
y = 200
x, y = y, x
print("x: ", x," y: ", y)
print()

# 8. 논리 연산자
is_admin = True
is_logged_in = False

print("관리자 & 로그인: ", is_admin and is_logged_in)
print("둘 중 하나: ", is_admin or is_logged_in)
print("로그인 안됨: ", not is_logged_in)
print()

# 9. 조건문 예제
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("로그인 성공")
else:
    print("로그인 실패ㅠ")
print()

# 10. 조건문 예제 (홀/짝)
number = 7

if number % 2 == 0:
    print("짝")
else:
    print("홀")
print()

# 11. 조건문 중첩 (점수 등급)
score = 92

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
print()