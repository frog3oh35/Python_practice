### 2025-07-05 리스트 확장 + 입력 다루기 및 복습
"""
# 1. 복습) 리스트 요소 모드 출력 (for문)
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 2. 복습) for + append
numbers = [1, 2, 3, 4, 5]
doubled = []

for n in numbers:
    doubled.append(n * 2)

print(doubled)

# 3. 복습) for문 + if
scores = [55, 70, 82, 45, 90]

for score in scores :
    if score >= 60:
        print(f"합격 : {score}")
    else:
        print(f"불합격 : {score}")
print()

# append() 기초
print("1. 리스트에 값 추가하기")
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)
print()

# input().split()기초
# .split() -> 공백 기준으로 나눔
print("2. 문자열 여러 개 입력받기")
text = input("단어 3개를 입력하세용: ")
words = text.split()
print(words)
print()

# map(int, input().split()) 응용
# list(map(...))로 꼭 감싸야 리스트로 출력 가능
# list() 일부러 안 감싸면 error 뜸! 이터레이터 / 이터러블 공부
print("3. 숫자 5개를 입력받아 int로 변환")
nums = list(map(int, input("숫자 5개를 입력: ").split()))
print(nums)
print()

# for + map() 같이 쓰기
print("4. 입력받은 숫자 각각 2배 출력")
for x in map(int, input("숫자 여러 개 입력: ").split()):
    print(x * 2)
"""



# Quiz 1. append() 복습
number = []

for i in range(3):
## 여기서 막힘;;
    i = int(input("입력하세욧: "))
    number.append(i)
print(number)
print()

# Quiz 2. input().split() + map() 활용
print("여러 개의 숫자를 입력하세요: ")
for x in map(int, input().split()):
    if x % 2 == 0:
        print(x)
print("===refactor code line===")

## refactoring code - list comprehension
numbers = list(map(int,input("숫자 입력: ").split()))
even_numbers = [x for x in numbers if x % 2 == 0]

for num in even_numbers:
    print(num)
print()

# Quiz 3. for x in map(...) 활용
for y in map(int, input("여러 개의 정수를 입력하세요: ").split()):
    print(y ** 2)
print("===refactor code line===")

## refactoring code - list comprehension
numbers = map(int, input("여러 정수 입력: ").split())
square_num = [z**2 for z in numbers]

for n in square_num:
    print(n)