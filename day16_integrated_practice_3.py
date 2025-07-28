### 2025-07-28
### 통합 문법 실습 3일차...


## Student 클래스 기반 등수 시스템

# 속성 : 이름, 학년, 과목-점수 딕셔너리
# 메서드 : 평균 계산, __lt__ 오버로딩
# 기능 : 전체 정렬, 학년별 정렬, 출력 포맷 구성

class Student:
    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = grade
        self.subjects = subjects # 딕셔너리

    def get_average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def __str__(self):
        return f"{self.name} | 학년 : {self.grade} | 평균 : {self.get_average():.2f}"

students = [
    Student("연하", 6, {"자료구조": 90, "운영체제": 75, "파이썬": 80}),
    Student("관희", 4, {"자료구조": 100, "운영체제": 85, "파이썬": 93}),
    Student("토끼", 4, {"자료구조": 100, "운영체제": 41, "파이썬": 63}),
    Student("개굴", 4, {"자료구조": 66, "운영체제": 89, "파이썬": 50}),
    Student("한비", 3, {"자료구조": 90, "운영체제": 90, "파이썬": 100}),
    Student("먀옹", 2, {"자료구조": 67, "운영체제": 87, "파이썬": 90}),
    Student("재희", 3, {"자료구조": 70, "운영체제": 100, "파이썬": 82}),
    Student("수달", 2, {"자료구조": 50, "운영체제": 78, "파이썬": 57}),    Student("피츄", 3, {"자료구조": 80, "운영체제": 37, "파이썬": 94}),
]

# 전체 평균점수 기준 정렬
print("🎖️ 전체 등수 (평균 기준):")
for rank, student in enumerate(sorted(students, reverse=True), 1):
    print(f"{rank}등 - {student}")
print()

# 학년 별 정렬
target_grade = 3
filtered = list(filter(lambda s : s.grade == target_grade, students))
print(f"📚 {target_grade}학년 등수:")
for rank, student in enumerate(sorted(filtered, reverse=True), 1):
    print(f"{rank}등 - {student}")

print()
print()

## Product 클래스 기반 인기 상품 정렬기

# 속성 : 이름, 가격, 수량, 카테고리
# 메서드 : get_sales() 가격 x 수량, __lt__(), __str__()
# 기능 : 상품 목록 생성 -> sorted로 전체 인기순 정렬 -> 특정 카테고리 filter -> 그 리스트도 인기순 정렬

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def get_sales(self):
        return self.price * self.quantity

    def __lt__(self, other):
        return self.get_sales() < other.get_sales()

    def __str__(self):
        return f"{self.name} | 카테고리 : {self.category} | 매출 : {self.get_sales()}"

products = [
    Product("가나디인형", 32000, 50, "인형"),
    Product("레니니인형", 12000, 30, "인형"),
    Product("감자칩", 1500, 180, "과자"),
    Product("토마토캔디", 3000, 120, "과자"),
    Product("노트", 3000, 83, "필기구"),
    Product("다색펜", 8000, 75, "필기구"),
    Product("우주먼지", 20000, 41, "인형"),
]

print("🎖️ 전체 인기순 상품:")
for rank, p in enumerate(sorted(products, reverse = True), 1):
    print(f"{rank}위 = {p}")
print()

# 특정 카테고리별 인기순
target = "인형"
filtered = list(filter(lambda p : p.category == target, products))

print(f"🧸 {target} 카테고리 인기순:")
for rank, p in enumerate(sorted(filtered, reverse = True), 1):
    print(f"{rank}위 - {p}")