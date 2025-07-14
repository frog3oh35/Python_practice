### 2025-07-14 예외 처리 기초
# 오류(error)가 발생하면 우아하게 처리해보자고...

"""
기본구조
try:
    실행할 코드
except 오류타입:
    예외 발생 시 실행할 코드


# 예제 코드 1
try: 
    print(10 / 0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
print()

# 여러 개의 except 처리
try:
    num = int(input("숫자 입력: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로 나누면 안돼요.")
except ValueError:
    print("숫자가 아닌 값을 입력했어요.")
print()


# else & finally
try:
    num = int(input("숫자 입력: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로 나누면 안돼요.")
except ValueError:
    print("숫자가 아닌 값을 입력했어요.")
else:
    print("정상적으로 처리되었습니다.")
finally:
    print("프로그램 종료.")

print()

# 사용자 정의 에러
raise ValueError("값이 잘못되었습니다!")
print()

"""


# 예제 1. ZeroDivisionError
try:
    x = int(input("나눌 숫자를 입력하세요: "))
    print("10 /", x, "=", 10 / x)
except ZeroDivisionError:
    print("‼️ 0으로 나눌 수는 없습니다.")
print()

# 예제 2. 숫자 입력받기 + 두 가지 예외 처리
try:
    user_input = input("숫자를 입력하세요: ")
    num = int(user_input)
    result = 100 / num
    print("100 /", num, "=", result)
except ZeroDivisionError:
    print("! 0으로 나눌 수 없다고")
except ValueError:
    print("! 숫자가 아니라고")
print()

try:
    n = int(input("점수 입력: "))
    print("n의 제곱:", n ** 2)
except ValueError:
    print("! 정소가 아닌 값인데")
finally:
    print("🎈 프로그램 종료!")