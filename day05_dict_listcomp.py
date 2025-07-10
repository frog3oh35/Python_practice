
### 2025-07-10 딕셔너리 심화, 리스트 컴프리헨션 조건식 포함

## 딕셔너리 심화 : 기본 반복 - for key in dict
# 기본적으로 for key in dict는 key만 반복
# 값을 꺼낼 땐 dict[key]로 접근

person = {
    "이름" : "연하",
    "나이" : 27,
    "mbti" : "ISFJ"
}

for key in person:
    print(key, ":", person[key])
print()


# 키와 값 동시에 반복
for key, value in person.items():
    print(f"{key} -> {value}")
# .items()는 (key, value) 튜플을 꺼냄
# 언팩킹 형태로 받아서 깔끔한 코드
print()


# .get() - 키로 값 꺼내되, 없는 경우 대비
print(person.get("mbti"))
print(person.get("주소"))
print(person.get("주소", "없음"))
# .get()은 키가 없을 때 에러 대신 기본값 반환
print()


# 'key' in dict - 키 존재 여부 확인
if "이름" in person:
    print("이름이 있습니다.")

if "주소" not in person:
    print("주소는 아직 없습니다.")



#practice
print("==mini practice==")
ice = {
    "제품명" : "메로나",
    "유통기한" : 250809,
    "상품코드" : "DL342M44",
    "회사" : "빙그레"
}

for key in ice:
    print(key, ":", ice[key])
print()

for key, value in ice.items():
    print(f"{key} => {value}")
print()

print(ice.get("회사"))
print(ice.get("생산지"))
print(ice.get("생산지", "없음"))
print()

if "제품명" in ice:
    print("제품명이 있습니다")

if "성분" not in ice:
    print("성분은 없어요")


## 조건식이 있는 리스트 컴프리헨션
# 조건 필터만 있는 경우
nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
print(even)
print()

# if-else
# [값1 if 조건 else 값2 for 항목 in 반복가능한 것]
# 주의 : if-else는 표현식 쪽에 들어감, 일반 if랑 순서가 다름
nums = [1, 2, 3, 4, 5]
result = [str(x) if x % 2 == 0 else "홀수" for x in nums]
"""이해가 안 될 땐 일반 for문으로 바꿔보자
result = []
for x in nums:
    if x % 2 == 0:
        result.append(str(x))
    else:
        result.append("홀수")
"""
print(result)


## Quiz 1
words = ["hi", "sun", "apple", "no", "day"]
three_words = [word for word in words if len(word) >= 3]
print(three_words)
print()

## Quiz 2
nums = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else 0 for x in nums]
print(result)
print()

## 만약 숫자가 str 형이면
nums = ["1", "2", "3", "4", "5"]
nums = list(map(int, nums))
# 여기에서 형변환
print(nums)
result = [x if x % 2 == 0 else 0 for x in nums]
print(result)