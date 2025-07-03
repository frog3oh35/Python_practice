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
#타입 명시가 중요한 경우에는 입력도 float로 한다
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

# 12. 자판기 메뉴 출력기
menu = "콜라"
money = 1500

if menu == "콜라":
    price =  1000
elif menu == "사이다":
    price = 1200
else :
    price = 1500

if money >= price:
    print(menu, "구매 완료!")
else :
    print("잔액 부족!")
print()

## Quiz 1
nameQ = "여나"
ageQ = "27"
food = "붕어싸만코"
print("안녕하세요! 제 이름은 " + nameQ + "입니다.")
print("나이는 " + ageQ + "살이고, 좋아하는 음식은 " + food + "입니다.")
print()

## Quiz 2
numnum = 33

if numnum % 2 == 0:
    print("짝수입니다")
else :
    print("홀수입니다")
print()

## Quiz 3

## Quiz 4
correct_username = "yeonha"
correct_password = "1234"

username = input("input username: ")
password = input("input password: ")

if correct_username == username and correct_password == password:
    print("로그인 성공!")
else:
    print("로그인 실패!")
print()

## Quiz 4
age1 = 33
has_ticket1 = True

age2 = 21
has_ticket2 = False

if age1 >= 20 and has_ticket1 == True:
    print("입장 가능")
else :
    print("입장 불가")
if age2 >= 20 and has_ticket2 == True:
    print("입장 가능")
else :
    print("입장 불가")
print()


## Quiz 5
score2 = int(input("점수를 입력하세요: "))

if score2 >= 90:
    grade = "A"
elif score2 >= 80:
    grade = "B"
elif score2 >= 70:
    grade = "C"
else :
    grade = "F"

print()
#output
print("당신의 점수는 " + str(score2) + "점, " + grade + "학점입니다.")
#f-string format
print(f"당신의 점수는 {score2}점, {grade}학점입니다.")


"""
 Quiz 5 refactoring


1. input()은 기본적으로 문자열
=> 숫자 비교시 반드시 int()로 감싸줘야 함
2. 근데 또 출력할 때는? "문자열" + 숫자 => python에서 error
=> "문자열" + "문자열"만 가능, str()로 다시 감싸줘야 함
3. 그래서 나온게 f-string format

4. 숫자가 0~100 범위 안에 있는지 확인해야 하니까!
if 0 <= score <= 100:
    # 학점 계산
else:
    print("0부터 100사이의 점수만 입력해주세요")
=> 실전에서 중요!
"""