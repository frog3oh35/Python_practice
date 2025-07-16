# Quiz 1. set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 공통된 원소만 출력되도록 set 연산을 수행하세요
result = set(a & b)
print(result)
print()

# Quiz 2. lambda 심화 - 점수 높은 순 + 이름 사전순 저열
students = [
    ("Jisoo", 85),
    ("Eunha", 92),
    ("Minho", 92),
    ("Sora", 78)
]

sorted_students = sorted(students, key=lambda x : (-x[1], x[0]))
print(sorted_students)
print()

# Quiz 3. 예외처리 - 입력값 검사 + 에러 핸들링
"""
try:
    x = int(input("첫 번째 숫자: "))
    y = int(input("두 번째 숫자: "))
    print("결과:", x / y)
except ValueError:
    print("숫자를 입력하세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
finally:
    print("프로그램 종료")
print()
"""

# Quiz 4
set_a = {2, 4, 6, 8, 10}
set_b = {1, 2, 3, 4, 5, 6}
result = set_a & set_b
print(result)
print()

# Quiz 5
students = [
    ("Yuna", 90),
    ("Arin", 95),
    ("Sana", 90),
    ("Nari", 100)
]

sorted_s = sorted(students, key = lambda x : (-x[1], x[0]))
print(sorted_s)
print()

# Quiz 6
try:
    x, y = map(int, input("숫자를 두개 입력하세요: ").split())
    print("결과: ", x / y)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except ValueError:
    print("숫자를 입력하세요")
finally:
    print("끝~~")