import json

# Quiz 1. 사용자 정의 예의 만들기 + raise

def check_age(num):
    if num < 0:
        raise ValueError("나이는 1 이상이어야 합니다! \n")
    print(f"당신의 나이는 {num}세입니다.\n")

try:
    user_input = input("나이를 입력하세요: ")
    num = int(user_input)
    check_age(num)
except ValueError as e:
    print("예외 발생:", e)


# Quiz 2. try~except + else
try:
    x, y = map(int, input("숫자 두 개를 입력해라: ").split())
    result = x / y
except ZeroDivisionError:
    print("0으로 나눌 수 없어요.")
else:
    print("정상 실행 결과:", result)
finally:
    print("연산 끝! \n")


# Quiz 3. 예외 객체 정보 확인
try:
    x = int(input("정수를 입력하세요: "))
except ValueError as e:
    print(e.args)
print()

# Quiz 4. 텍스트 파일에 저장
f = open("message.txt", "w", encoding="utf-8")
f.write(input("입력하세용: "))
f.close()

# Quiz 5. JSON
json_str = {
    "name": "연하",
    "age": 27,
    "job": "QA"
}

with open("jso_str.json", "w", encoding="ut-08") as f:
    json.dump(json_str, f)

with open("json_str.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["age"])