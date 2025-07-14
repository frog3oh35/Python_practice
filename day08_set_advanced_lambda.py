### 2025-07-14 집합(Set) + lambda 함수 심화

## 집합(set) - 집합 기초
# 집합은 중복을 허용하지 않는 자료형
my_list = [1, 2, 3, 4, 4, 6, 3]
my_set = set(my_list)

print("기존 리스트:", my_list)
print("중복 제거된 집합:", my_set)
print()



## 집합(set) - 집합 메서드 기본
fruits = set()

# 원소 추가
fruits.add("apple")
fruits.add("banana")
print("과일 집합:", fruits)

# 원소 제거
fruits.remove("banana")
print("바나나 제거 후:", fruits)

# 존재하지 않는 원소 제거 (오류 없이)
# remove 쓰면 에러
fruits.discard("graph")
print("discard 사용 후:", fruits)
print()


## 집합(set) - 집합 연산
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "graph"}

print("합집합:", set1 | set2)
print("교집합:", set1 & set2)
print("차집합:", set1 - set2)
print("대칭차집합:", set1 ^ set2)
print()


## lambda + sorted 정렬 심화
words = ["banana", "fig", "apple", "kiwi"]
sorted_by_length = sorted(words, key=lambda x: len(x))

print("길이 기준 정렬:", sorted_by_length)
print()


# 예제 : 학생 점수 & 이름 정렬

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 90)
]

sorted_students = sorted (
    students,
    key = lambda x : (-x[1], x[0])
)

print("학생 정렬 결과:", sorted_students)
print()

numbers = [7, 4, 1, 10, 3, 8, 2]
sorted_numbers = sorted(numbers, key=lambda x : x % 2)

print("짝수 우선 정렬:", sorted_numbers)