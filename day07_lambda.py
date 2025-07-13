### 2025-07-13 lambda 함수

## 람다 함수 기본 구조
# lambda 매개변수 : 리턴값
# def 없이도 함수처럼 동작함
# 익명 함수 -> 보통 변수에 담아서 사용함

# 예제 1: 1더하기 함수
add_one = lambda x : x + 1
print(add_one(5))

# 예제 2 : 두 수 더하기
add = lambda a, b : a + b
print(add(5, 2))
print()


## 람다 함수 vs 일반 함수 비교
# 예제 1 : 같은 기능 비교

# 일반 함수
def square(x):
    return x ** 2

# 람다 함수
square_lambda = lambda a : a ** 2

print("normal func :", square(4))
print("lambda func :", square_lambda(7))
print()

# sorted에 람다 함수 사용
words = ["banana", "apple", "cherry", "date"]

# 기본 구조 sorted(리스트, key = 정렬기준 함수)
sorted_words = sorted(words, key=lambda word : len(word))

print(sorted_words)
print()


## 계산기, 정렬, map, filter 활용

# map() 함수 - 일괄 변환
# map(함수, iterable)
# map객체 -> list로 감싸서 써야 눈에  보임
nums = [1, 2, 3, 4]
doubled = list(map(lambda x : x * 2, nums))
print(doubled)
print()

# filter() 함수 - 조건 필터링
# filter(함수, iterable)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x : x % 2 == 0, nums))

print(evens)
print()

# mini Quiz_1
print("===map() and filter() mini Quiz===")
number = [2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12]

triple = list(filter(lambda x : x % 3 == 0, number))
square_triple = list(map(lambda y : y ** 2, triple))

print(square_triple)
print()

# mini Quiz_2
print("===sorted() and lambda mini Quiz===")

students = [
    ("alice", 82),
    ("bob", 95),
    ("diana", 76),
    ("charlie", 89)
]

sorted_score = sorted(students, key=lambda x : x[1], reverse=True)
print(sorted_score)