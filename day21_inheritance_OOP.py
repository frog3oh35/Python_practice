### 2025-08-19
## 상속 + OOP

class TestCase:
    def __init__(self, case_id, descript, time, success):
        self.case_id = case_id
        self.descript = descript
        self.time = time
        self.success = success

    def __str__(self):
        status = "✅" if self.success else "✖️"
        return f"{self.case_id} | {self.descript} | {self.time}s | {status}"

class ApiTestCase(TestCase):
    def __init__(self, case_id, descript, time, success, endpoint):
        super().__init__(case_id, descript, time, success)
        self.endpoint = endpoint

    def __str__(self):
        status = "✅" if self.success else "✖️"
        return f"[API] {self.case_id} | {self.descript} | {self.time}s | {status}"

class UiTestCase(TestCase):
    def __init__(self, case_id, descript, time, success, screen):
        super().__init__(case_id, descript, time, success)
        self.screen = screen

    def __str__(self):
        status = "✅" if self.success else "✖️"
        return f"[UI] {self.case_id} | {self.descript} | {self.time}s | {status}"

class QAProject:
    def __init__(self, name, test_cases):
        self.name = name
        self.test_cases = test_cases

    def show_all(self):
        print(f"\n✨ 프로젝트: {self.name}")
        for tc in self.test_cases:
            print(tc)


if __name__ == "__main__":
    tc1 = TestCase("TC-01", "로그인 성공", 1.2, True)

    tc2 = ApiTestCase("TC-02", "회원가입 API", 0.8, False, "/api/signup")
    tc3 = UiTestCase("TC-03", "로그인 화면 버튼 클릭", 2.4, True, "LoginScreen")

    project = QAProject("상속 연습 프로젝트", [tc1, tc2, tc3])

    project.show_all()