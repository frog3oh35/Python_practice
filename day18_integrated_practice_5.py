### 2025-07-31
## 객체지향 + 통합 문법 연습 5일차 될 때까지 반복 연습 간다!!!

# 라이브러리 대출 시스템
class Book:
    def __init__(self, name, author, genre, year, is_available):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if self.is_available == True:
            self.is_available = False
            print(f"{self.name} 대출 성공!")
        else:
            print(f"{self.name}은 이미 대출 중입니다.")

    def return_book(self):
        print(f"{self.name} 반납 완료")
        self.is_available = True

    def __str__(self):
        return f"{self.name} | {self.author} | {self.year}"

b1 = Book("모비딕", "허먼 멜빌", "문학", 1851, False)
b2 = Book("S를 좋아하는 수상한 여성", "여나", "에세이", 2025, True)
b3 = Book("토익 Vocabulary", "토익북", "어학", 2018, True)
b4 = Book("인프라 마스터", "IT출판", "기술", 2021, False)
b5 = Book("스크럼의 기술", "IT출판", "기술", 2023, True)

books = [b1, b2, b3, b4, b5]

# 대출 가능한 책만
filter_available = list(filter(lambda b : b.is_available, books))
for book in filter_available:
    print(book)
print()

# 출판 연도별 정렬
sorted_books = sorted(books, key = lambda b : b.year, reverse=True)
for book in sorted_books:
    print(book)

# 클래스 인스턴스를 print()하려면 __str__() 필요
# 이터러블 전체를 print()하려는 순간 __repr__() 필요해짐
# 이건 파이썬 클래스 인스턴스일 때 문제로, 다른 언어는 다른 로직으로 동작함