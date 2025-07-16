### 2025-07-16 예외 처리 심화
## else, finally, raise
## 사용자 정의, e.args, type(e)
## log 및 traceback

import traceback

## else, finally 실습
def devide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요")
    else:
        print("정상 실행 결과:", result)
    finally:
        print("연산 종료 \n")

devide(10, 2)
devide(5, 0)
# else는 예외가 발생하지 않을 때만 실행

## raise로 예외 직접 발생시키기
# raise는 조건에 따라 예외를 인위적으로 발생시킬 때 사용한다. 유효성 검사, 커스텀 로직 제어 등

def check_age(age):
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다.")
    print(f"당신의 나이는 {age}세입니다.")

try:
    check_age(-5)
except ValueError as e:
    print("예외 발생:", e)
print()


## 사용자 정의 예외 만들기
class MyCustomError(Exception):
    pass

def do_something(value):
    if value == "bad":
        raise MyCustomError("나쁜 값이 들어왔어요!")
    print("정상 동작 완료")

try:
    do_something("bad")
except MyCustomError as e:
    print("사용자 정의 예외 처리:", e)
print()

## e.args로 상세 정보 보기
try:
    int("abc")
except ValueError as e:
    print("e.args:", e.args)
# args는 예외 메세지들을 튜플로 반환
# 예외 메세지가 복수일 수 도 있기 때문
print()

## type(e)로 예외 타입 확인
try:
    1 / 0
except Exception as e:
    print("에러 타입:", type(e))
print()

## 로그로 저장하기
try:
    do_something()
except Exception as e:
    with open("error_log.txt", "w") as f :
        f.write(f"에러 타입: {type(e)}\n")
        f.write(f"에러 메세지: {str(e)}\n")
print()
"""
## traceback
try:
    1 / 0
except Exception:
    traceback.print_exc()
    #터미널에 자세한 에러 정보 출력
"""