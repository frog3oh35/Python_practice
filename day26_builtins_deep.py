import math
import random
from datetime import datetime, timedelta, date

print("=== math 모듈 심화 ===")

# 기본 연산
print("제곱 pow(2, 5):", math.pow(2, 5))
print("제곱근 sqrt(81):", math.sqrt(81))

# 반올림 관련
print("올림 ceil(4.2):", math.ceil(4.2))
print("내림 floor(4.8):", math.floor(4.8))
print("절댓값 fabs(-3.14):", math.fabs(-3.14))

# 로그, 삼각함수
print("log10(1000):", math.log10(1000))
print("sin(90도):", math.sin(math.radians(90)))

# 최대공약수
print("gcd(24, 36):", math.gcd(24, 36))

# 상수
print("PI:", math.pi)
print("E:", math.e)


print("\n=== random 모듈 심화 ===")
# 기본 난수
print("0~1 사이 난수:", random.random())
print("1~10 사이 정수:", random.randint(1, 10))

# 시드 고정 (결과 재현 가능)
random.seed(42)
print("seed(42) 이후 random():", random.random())

# 리스트 섞기
cards = ["A", "B", "C", "D", "E"]
random.shuffle(cards)
print("shuffle 결과:", cards)

# 여러 개 샘플 추출
nums = list(range(1, 46))
lotto = random.sample(nums, 6)
print("로또 번호:", lotto)

# 시뮬레이션: 주사위 두 개 굴리기
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"🎲  주사위 결과: {dice1} + {dice2} = {dice1 + dice2}")


print("\n\n=== datetime 모듈 심화 ===")

# 현재 시각
now = datetime.now()
print("현재 시각:", now)

# 날짜 포맷
print("날짜 포맷:", now.strftime("%Y-%m-%d %H:%M:%S"))

# D-Day 계산
target = datetime(2023, 3, 9)
diff = target - now
print("뾰로롱:", diff.days, "일")

# 날짜 더하기 / 빼기
one_week = timedelta(days=7)
print("7일 후:", now + one_week)
print("7일 전:", now + one_week)

# 오늘 날짜만 가져오기
today = date.today()
print("오늘:", today)

# 7일치 날짜 리스트 만들기
dates = [today + timedelta(days=i) for i in range(7)]
print("이번 주 날짜들:", dates)