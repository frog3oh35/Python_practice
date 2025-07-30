### 2025-07-30 : 통합 문법 실습 4일차... 아직도 객체지향이 슬프다

## 날짜 필터기용 클래스 
"""
class WeatherData :
    def __init__(self, city, temperatures):
        self.city = city
        self.temperatures = temperatures # 리스트
    
    def get_average(self):
        return sum(self.temperatures) / 7

    def __str__(self):
        return f"{self.city} | 평균기온: {self.get_average():.1f}"

wData = [  
    WeatherData("서울", [30, 31, 33, 35, 32, 35, 34]),
    WeatherData("대전", [32, 33, 35, 36, 36, 35, 33]),
    WeatherData("대구", [37, 35, 34, 36, 37, 37, 34]),
    WeatherData("광주", [32, 33, 30, 35, 30, 29, 34]),
    WeatherData("세종", [32, 33, 36, 35, 35, 37, 31]),
    WeatherData("인천", [29, 30, 33, 34, 33, 33, 31]),
    WeatherData("제주", [28, 30, 27, 29, 30, 29, 27])
]

# 전체 도시 평균 온도 기준 정렬

# 더운 도시만!
hot_cities = list(filter(lambda w : w.get_average() >= 33, wData))

for city in hot_cities:
    print(city)
print()

# 전체 도시 평균기온 순 정렬
sorted_cities = sorted(wData, key = lambda w : w.get_average(), reverse = True)

for rank, city in enumerate(sorted_cities, 1):
    print(f"{rank}위 - {city}")
print()

# 최고기온이 가장 높은!
hottest_city = max(wData, key=lambda w: max(w.temperatures))
print(f"🔥 이번 주 최고기온 도시 : {hottest_city.city} ({max(hottest_city.temperatures)}도)")
print()

target = input("검색할 도시명을 입력하세요: ")
result = list(filter(lambda w: w.city == target, wData))

if result:
    print(result[0])
else:
    print("😸 그런 도시는 없습니다.")
"""


## 장학생 추출기

class Student:
    def __init__(self, name, grade, scores, club):
        self.name = name
        self.grade = grade
        self.scores = scores # 딕셔너리
        self.club = club

    def get_average(self):
        return sum(self.scores.values()) / len(self.scores)

    def is_scholarship_eligible(self):
        return self.get_average() >= 80 and self.club == True

    ## __lt__() 오버로딩 복습 필요
    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def __str__(self):
        return f"이름: {self.name} | 학년: {self.grade} | 평균: {self.get_average():.1f} | 장학생 여부: {self.is_scholarship_eligible()}"

students = [
    Student("연하", 4, {"OS": 65, "PM": 77, ".NET": 88}, False),
    Student("토끼", 3, {"OS": 95, "PM": 47, ".NET": 78}, False),
    Student("코끼리", 4, {"OS": 53, "PM": 95, ".NET": 66}, True),
    Student("개굴", 3, {"OS": 88, "PM": 100, ".NET": 40}, True),
    Student("토마토", 4, {"OS": 80, "PM": 74, ".NET": 90}, True),
    Student("천사", 3, {"OS": 78, "PM": 81, ".NET": 88}, False),
    Student("해파리", 2, {"OS": 72, "PM": 47, ".NET": 90}, True),
    Student("토끼리", 2, {"OS": 90, "PM": 77, ".NET": 98}, True)
]

## 장학생 리스트 뽑기
filtered_scholar = list(filter(lambda s: s.is_scholarship_eligible(), students))
print("👨‍🎓 장학생 명단")
for student in filtered_scholar:
    print(student)
print()

## 평균 점수 기준 정렬
print("🐰 평균 점수 기준 정렬")
for rank, stu in enumerate(sorted(students, reverse = True), 1):
    print(f"석차 : {rank} | {stu}")
print()