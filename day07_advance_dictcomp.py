### 2025-07-13 딕셔너리 컴프리헨션 심화

## 딕셔너리 컴프리헨션 심화

# dict_comp step1 : 딕셔너리 삼항 조건문
# 값에 따라 가공 로직이 바뀌는 경우를 처리하는 방법
# {key: (값1 if 조건 else 값2) for key, value in 딕셔너리.items()}

scores = {
    "연하" : 55,
    "정훈" : 90,
    "유정" : 23,
    "관희" : 59
}

result = {
    key : "Pass" if score >= 60 else "Fail"
    for key, score in scores.items()
}

print(result)
print()


# 예제 1 : 출석 상태 구분
attendance = {
    "alice" : True,
    "bob" : False,
    "charlie" : True,
    "diana" : False
}

status = {
    name: ("출석" if is_present else "결석") for name, is_present in attendance.items()
}

print(status)
print()


# dict_comp step 2 : key와 value 바꾸기
# 기존 딕셔너리에서 key <-> value 위치를 뒤집고 싶은 경우
# {value : key for key, value in 딕셔너리.items()}
original = {
    "apple" : "사과",
    "banana" : "바나나",
    "graph" : "포도"
}

reversed_dict = {
    value : key for key, value in original.items()
}

print(reversed_dict)
print()


# dict_comp step 3 : 데이터 가공 (조건 필터링, 값 가공)

# (1) 조건 필터링 구조
# {key : value for key, value in 딕셔너리.items() if 조건}
# (2) 값 계산 가공 구조
# {key : 계산된값 for key, value in 딕셔너리.items()} : value에 숫자 계산, 문자열 조작 등 원하는 로직 넣으면 됨

# 예제 1 : 10이상만 필터링
prices = {
    "item1" : 5,
    "item2" : 10,
    "item3" : 15,
    "item4" : 2,
    "item5" : 12
}

filtered = {
    k : v for k, v in prices.items() if v >= 10
}

print(filtered)
print()

# 예제 2 : 할인 적용하기
prices = {
    "item1" : 10000,
    "item2" : 20000,
    "item3" : 15000
}

discounted = {
    k : int(v * 0.8) for k, v in prices.items()
}

print(discounted)