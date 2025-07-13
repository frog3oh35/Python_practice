# Quiz 1. pop() & sort()

nums = [4, 1, 7, 3, 9]

print("min:", min(nums))
nums.remove(min(nums))

nums.sort(reverse = True)
print("내림차순 정렬:", nums)
print()

# Quiz 2. list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8]]

even_squares = [x ** 2 for row in matrix for x in row if x % 2 == 0]

print(even_squares)
print()

# Quiz 3. dictionary comprehension
data  = {'a': 5, 'b': 10, 'c': 15}
result = {key : value * 2 for key, value in data.items() if value >= 10}

print(result)
print()

# Quiz 4. *args를 활용한 누적 곱 합수
def multiply_all(*number):
    result = 1
    for num in number:
        result = result * num
        #refactor reulst *= num
    print(result)
# return 값 사용하여 재사용 가능하게 만드는 리디자인 코드도 써봐야함

multiply_all(2, 3, 4)
print()

# Quiz 4. refactor
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_all(2, 4, 5))
print()

# Quiz 5. **kwargs로 옵션 받아 출력
def print_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 오답 : print_config("debug" = True, "verbose" = False)
print_config(debug = True, verbose = False)
# 딕셔너리 같은 구조고 내부에서 딕셔너리로 처리되지만 전달한 때 딕셔너리 문법 ("key" = value)로 쓰면 안된다.ㅠㅠ