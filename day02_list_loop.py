# 1. List
"""
fruits = ["사과", "바나나", "딸기"]

print(fruits[0]) #indexing
print(fruits[0:2]) #slicing

fruits[1] = "포도"
print(fruits) #value update

fruits.append("오렌지")
print(fruits) #Add an item using append()

fruits.remove("사과")
print(fruits)

print()


# 2. for
for fruit in fruits: #for 변수 in 리스트... 여기서 변수가 새로 정의된다.
    print(fruit)

# 3. range()
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

print()

# 4. while
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# 5. List + for
scores = [85, 90, 92, 78, 100]

total = 0
for score in scores :
    total += score

average = total / len(scores)
print("총합: ", total)
print("평균: ", average)

# len
print(len("hello"))
"""

# Quiz 1.
foods = ["피자", "햄버거", "파스타", "초밥"]
print(foods[1])
print()

# Quiz 2.
animals = ["고양이", "강아지", "토끼", "다람쥐"]

for i in animals:
    print(i)
print()

# Quiz 3.
sum = 0

for i in range(1,11):
    sum += i

print(sum)
print()

# Quiz 4.
for j in range(1,21):
    if j % 2 == 0:
        print(j)
print()

print("###refactor code###")
## refactoring
for j in range (2, 21, 2):
    print(j)

print()

# Quiz 5.
scores = [85, 90, 78, 92, 100]
total = 0

for score in scores:
    total += score

average = total/ len(scores)

print(average)


"""
Quiz 3, 4
range() 에서 끝 숫자를 포함하지 않음

Quiz 3에서 sum은 파이썬 내장 함수와 겹치는 이름
=> total_sum 같은 변수명 추천!


Quiz 4에서 for i in range(2, 21, 2)를 사용하여
짝수만 순회! 

* index 접근
scroes = [85, 90, 78]
for i in range(len(scores)):
    print(i, scores[i]) #인덱스와 값 함께 보기
for idx, score in enumerate(scores):
    print(idx, score)

enumerate()란?
-> 리스트를 반복하면서, 인덱스 번호까지 같이 꺼내주는 함수

"""