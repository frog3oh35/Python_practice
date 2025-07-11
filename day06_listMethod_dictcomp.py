### 2025-07-11
### 리스트 메서드
### 리스트 컴프리헨션 : 조건식 심화
### 딕셔너리 : 컴프리헨션 기초

## 리스트 메서드
# pop() 특정 인덱스 요소를 제거 + 반환
print("== pop() ==")
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print("pop():", last)
print("남은 리스트:",fruits)

first = fruits.pop(0)
print("pop(0):", first)
print("남은 리스트:", fruits)
print()


# sort() 리스트 정렬, 원본이 변경됨
print("== sort() ==")
numbers = [5, 1, 8, 3, 9]
numbers.sort()
print("오름차순:", numbers)

numbers.sort(reverse=True)
print("내림차순:", numbers)
print()

# reverse() 리스트 순서만 뒤집음(정렬 아님) 역순 출력용
print("== reverse() ==")
letters = ["a", "b", "c", "d"]
letters.reverse()
print("역순:", letters)
print()

## 조건식 리스트 컴프리헨션 심화 (삼항/중첩)
# [결과 if 조건 else 다른결과 for 변수 in 반복가능한객체]

# 예제 1
nums = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else "홀수" for x in nums]
print(result)
print()

# 예제 2
scores = [85, 42, 77, 33, 90]

result = ["pass" if s >= 60 else "fail" for s in scores]
print(result)
print()


## 중첩 for문 리스트 컴프리헨션
# [표현식 for i in 리스트1 for j in 리스트2]

# 예제 1 두 리스트의 곱
print("== 중첩 for문 리스트 컴프리헨션 ==")
a = [1, 2, 3]
b = [10, 100]

result = [x * y for x in a for y in b]
print(result)
print()

# 예제 2 구구단 2~3단 만들기
result = [f"{i} x {j} = {i * j}" for i in range(2, 4) for j in range(1, 10)]
print(result)
print()


## Quiz 1
print("== Quiz 1 ==")
nums = [1, 3, 4, 6, 7, 9]
multi = ["3x" if x % 3 == 0 else x for x in nums]
print(multi)
print()

## Quiz 2
print("== Quiz 2 ==")
a = [1, 2]
b = [3, 4]
add = [f"{i} + {j} = {i + j}" for i in a for j in b]
print(add)
print()


## 딕셔너리 컴프리헨션 기본 문법
# {key_expr : value_expr for item in iterable}
print("== 예를 들어 1부터 5까지 제곱을 딕셔너리로 만들고 싶다? ==")
squares = {x : x ** 2 for x in range(1, 6) }
print(squares)
print()

# Quiz 1
letters = ['a', 'b', 'c']
result = {ch : ch.upper() for ch in letters}
print(result)
print()

# Quiz 2
nums = [1, 2, 3, 4, 5, 6]
evens = {num : num**2 for num in nums if num % 2 == 0}
print(evens)