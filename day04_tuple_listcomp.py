
### 2025-07-07 튜플 기초, 리스트 컴프리헨션 연습

## Tuple
# 리스트와 비슷하지만, 변경할 수 없는 자료형
# 고정된 값들을 다룰 때 사용

person = ("연하", 27, "ISFJ")
print(person)

print("이름:", person[0])
print("나이:", person[1])

name, age, mbti = person
# 언팩킹 (각 변수에 나눠 담기)
print(f"{name}, {age}, {mbti}")
print()


## list comprehension
# 한 줄로 리스트를 만들 수 있는 문법
# [표현식 for 항목 in 반복가능한객체]

print("# list comprehension exercise 1")
squares = [x ** 2 for x in range(1, 6)]
print(squares)
print()

print("# listcomp exercise 2")
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
print()

print("# listcomp exercise 3")
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)


## tuple basic & list comprehension Quiz

# Quiz 1 unpacking
print("# unpacking")
human = ("연하", 27, "ISFJ")
name, age, mbti = human
print(f"{name}님은 {age}살이고, {mbti}입니다.")
print()

# Quiz 2 tuple return
print("# tuple return")
def get_user_info():
    name, age = input("이름과 나이를 입력하세요: ").split()
    
    return (name, int(age))

user = get_user_info()
print(user)


# Quiz 3 listcomp 01
squares = [x ** 2 for x in range(1,11) if x % 2 == 1]
print(squares)

# Quiz 4 listcomp 02
words = ["apple", "hi", "banana", "yes", "watermelon"]
# wrong!! : five_len = [len(word) for word in words if len(word) >= 5]
five_len = [word for word in words if len(word) >= 5]
print(five_len)

# Quiz 5 listcomp 03
fruits = ["apple", "banana", "watermelon", "peach", "lemon"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)