### 2025-07-23 lambda reduce

## reduce() : 누적 연산을 수행하는 함수 (리스트 -> 하나의 값)

from functools import reduce

# 예제 1 곱하기 누적
nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print(product)
print()

# 예제 2 가장 긴 단어 찾기

words = ["cat", "tiger", "lion", "elephant"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)