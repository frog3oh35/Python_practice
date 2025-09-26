from functools import reduce
import random

# -------------
# 1. 클래스 & 상속 & 다형성
# -------------
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
        return f"{self.name}🐹: 멍멍!"

class Bunny(Animal):
    def speak(self):
        return f"{self.name}🐰: 끼요옷!"

# -------------
# 2. 리스트/딕셔너리 컴프리헨션
# -------------

numbers = [random.randint(1, 10) for _ in range(10)]
squares = [x**2 for x in numbers if x % 2 == 0]
cube_dict = {x: x**3 for x in numbers}

# -------------
# 3. 람다 + map/filter/reduce
# -------------

double = list(map(lambda x: x*2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a+b, numbers)

# -------------
# 4. 예외 처리 + 파일 I/O
# -------------

try:
    with open("day23_output.txt", "w", encoding="utf-8") as f:
        f.write("=== Python Day 종합 복습 ===\n\n")
        f.write(f"원본 numbers: {numbers}\n")
        f.write(f"짝수 제곱: {squares}\n")
        f.write(f"숫자^3 딕셔너리: {cube_dict}\n")        
        f.write(f"map 결과(2배): {double}\n")  
        f.write(f"filter 결과(짝수): {evens}\n") 
        f.write(f"reduce 합계: {total}\n")
        f.write(f"\n== 동물 클래스 테스트 ==\n")
        animals = [Dog("가나디", 3), Bunny("토깽이", 2)]
        for a in animals:
            f.write(str(a) + " -> " + a.speak() + "\n")

    print("🐰 day23_output.txt 파일에 결과 저장 완료!")  

except Exception as e:
    print("🐇 파일 처리 중 에러 발생: ", e)