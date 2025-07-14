# 복습 퀴즈
import random

# Quiz 1. sorted + lambda 
students = [
    ("alice", 78),
    ("Bob", 92),
    ("Charlie", 88),
    ("Alice", 85),
    ("David", 90)
]

sorted_score = sorted(students, key = lambda x : x[1], reverse=True)
print(sorted_score)
print()

# Quiz 2. filter + map
numbers = [random.randint(1, 30) for _ in range(10)]
triple = list(filter(lambda x : x % 3 == 0, numbers))
print(triple)
print()

# Quiz 3. dictionary comprehension
temp_data = {
    "Seoul": 32,
    "Busan": 27,
    "Incheon": 29,
    "Daegu": 34,
    "Gwangju": 26
}

hot_cold = ["Hot" if x >= 30 else "Cool" for x in temp_data.values()]
print(hot_cold)
print()

# Quiz 4. Lambda basic
add_five = lambda x : x + 5
double = lambda x : x * 2
print(add_five(10))
print(double(10))
print()

# Quiz 5. dictionary value changing 
price_data = {
    "apple": 1000,
    "banana": 800,
    "melon": 1200
}

discount = {
    k : int(v * 0.9) for k, v in price_data.items()
}

comp_dis = [v for v in price_data.values()]
blank_dis = [v for _, v in price_data.items()]
# 컴파일 에러 blank_dis_2 = [v for _, v in price_data.values()]

print(discount)
print()
print(comp_dis)
print(blank_dis)