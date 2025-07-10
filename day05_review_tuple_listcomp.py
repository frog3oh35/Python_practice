# Quiz 1
nums = [1, 2, 3, 4, 5, 6]

even = [x * 2 for x in nums if x % 2 == 0]
print(even)
print()

# Quiz 2
info = ("연하", 27, "ISFJ")
name, age, mbti = info
print(f"{name}의 나이는 {age}세이고, mbti는 {mbti}다.")
print()

# Quiz 3
def person():
    name, age = input("이름과 나이를 입력하세요: ").split()
    return (name, int(age))

user = person()

print(user)
print()

# Quiz 4
words = ["hi", "banana", "apple", "yes", "map"]

four_word = [word for word in words if len(word) >= 4]
print(four_word)