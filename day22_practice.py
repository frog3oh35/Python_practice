from functools import reduce
import random

# 1. 복습... OOP

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: 멍멍"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: 애옹"

# --------------
# 2. 복습... 컴프리헨션

numbers = [random.randint(1, 10) for _ in range(10)]
squares = [x**2 for x in numbers if x % 2 == 0]
number_dict = {x: x**3 for x in numbers}

# --------------
# 3. lambda + map/filter/reduce

double = list(map(lambda x: x*2, numbers))
even_only = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = reduce(lambda a, b: a+b, numbers)

# --------------
# 4. 예외 처리 +

try :
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"==Python 복습 종합==\n")
        f.write(f"원본 numbers: {numbers}\n")
        f.write(f"짝수 제곱: {squares}\n")
        f.write(f"숫자^3 딕셔너리: {number_dict}\n")
        f.write(f"배수 map 결과: {double}\n")
        f.write(f"짝수 filter 결과: {even_only}\n")
        f.write(f"reduce 합계: {sum_all}\n")
except Exception as e:
    print("파일 처리 중 에러 발생:", e)


animals = [Dog("가나디", 3), Cat("고영희", 2)]
for a in animals:
    print(a, "->", a.speak())