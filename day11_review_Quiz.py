### 2025-07-17

# list comprehension

num = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

result = [x ** 2 if x % 2 == 1 else "even" for x in num]

print(result)
print()

# list comprehension (for)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

trans = [[row[i] for row in matrix] for i in range(3)]
print(trans)
## 복습 필요!!ㅠㅠ

print()

# *args **kwargs
def describe(*args, **kwargs):
    print("이름 목록:", args)
    print("추가 정보:", kwargs)

describe("연하", "오빠추", 성격 = "다정함", 직업 = "QA")
print()


# dictionary comprehension
nums = [1, 2, 3, 4, 5, 6]
dict = {key : "짝수" for key in nums if key % 2 == 0}
print(dict)
print()


# lambda + filter
words = ["cat", "tiger", "dog", "lion", "wolf", "bear", "ant"]

mini_words = list(filter(lambda x : len(x) <= 4, words))
print(mini_words)
print()

# exception handling
def devide_by_two(user_input):
    try:
        number = int(user_input)
        result = number / 2
    except ValueError:
        print("ValueError! 숫자를 입력해주세요.")
    else:
        print("정상 결과:", result)
    finally:
        print("작업 완료")

devide_by_two(input("입력하세요: "))