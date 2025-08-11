### 2025-08-11
## 느슨했던 파이썬을 다시 하다...

class TestCase:
    def __init__(self, case_id, descript, time, success):
        self.case_id = case_id
        self.descript = descript
        self.time = time
        self.success = success

    def __str__(self):
        status = "✔️" if self.success else "✖️"
        return f"{self.case_id} | {self.descript} | {self.time} | {status}"

class QAproject:
    def __init__(self, name, deadline, cost, test_cases):
        self.name = name
        self.deadline = deadline
        self.cost = cost
        self.test_cases = test_cases

    def get_avg_time(self):
        return sum(tc.time for tc in self.test_cases) / len(self.test_cases)

    def get_failed_cases(self):
        return [tc for tc in self.test_cases if not tc.success]

    def get_slow_cases(self, threshold=2.0):
        return [tc for tc in self.test_cases if tc.time >= threshold]
    
    def find_case_by_id(self, case_id):
        return next((tc for tc in self.test_cases if tc.case_id == case_id), None)

tc1 = TestCase("TC-01", "로그인 성공", 1.2, True)
tc2 = TestCase("TC-02", "로그인 실패", 0.8, False)
tc3 = TestCase("TC-03", "응답 지연", 2.4, False)
tc4 = TestCase("TC-04", "비밀번호 오류", 1.5, True)

project = QAproject(
    "로그인 API 테스트",
    "2025-08-31",
    1000,
    [tc1, tc2, tc3, tc4]
)

print(f"** 프로젝트 : {project.name}")
print(f"* 전체 테스트 케이스")
for tc in project.test_cases:
    print(tc)

print(f"\n* 평균 실행 시간 : {project.get_avg_time():.2f}초")

print(f"\n* 실패 케이스 : ")
for tc in project.get_failed_cases():
    print(tc)

print(f"\n* 느린 케이스(2.0초 이상) : ")
for tc in project.get_slow_cases():
    print(tc)

print("\n** ID 검색 : ")
result = project.find_case_by_id("TC-03")
print(result if result else "해당 ID 없음")