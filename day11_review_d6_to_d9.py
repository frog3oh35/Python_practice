### 2025-07-18
### day 6 ~ day 9
### 리스트컴프리헨션, 딕셔너리 컴프리헨션, 가변 인자, 람다 함수, 예외처리 복습

# 리스트컴프리헨션 삼항
nums = [1, 2, 3, 4, 5]
result = ["짝수" if n % 2 == 0 else "홀수" for n in nums]

print(result)
print()

# 중첩 리스트 컴프리헨션

matrix = [[i * j for j in range(1,4)]for i in range(1, 4)]

print(matrix)
print()

# *args, **kwargs
def show(*args, **kwargs):
    print(args)
    print(kwargs)
show(1, 2, 3, name = "연하", job = "QA")
print()

# Lambda + sorted
words = ["apple", "banana", "kiwi"]
print(sorted(words, key = lambda x : len(x)))
print()

# 예외처리 기본
try:
    x = int("a")
except ValueError as e:
    print("에러 발생:", e)
finally:
    print("마무리하기")