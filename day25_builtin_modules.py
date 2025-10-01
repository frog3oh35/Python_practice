import os 
import sys
import math
import random
import datetime

print("=== Built-in Modules Demo ===")

# 1. os : 운영체제와 상호작용
print("\n[os 모듈]")
print("현재 작업 디렉토리:", os.getcwd())
print("현재 디렉토리 안 파일들:", os.listdir("."))

# 2. sys : 파이썬 시스템 정보
print("\n[sys 모듈]")
print("Python version: ", sys.version)
print("실행 파일 경로: ", sys.executable)

# 3. math : 수학 계산
print("\n[math 모듈]")
print("제곱근 sqrt(25): ", math.sqrt(25))
print("팩토리얼 5!: ", math.factorial(5))
print("원주율: ", math.pi)

# 4. random : 난수 생성
print("\n[random 모듈]")
print("0~1 사이 난수:", random.random())
print("1~10 사이 정수 난수 :", random.randint(1, 10))
print("리스트에서 랜덤 추출:", random.choice(['🐰', '🐙', '🐨']))

# 5. datetime : 날짜와 시간
print("\n[datetime 모듈]")
now = datetime.datetime.now()
print("현재 시각:", now)
print("올해 몇 주차인지:", now.isocalendar()[1])
print("날짜 포맷:", now.strftime("%y-%m-%d %H:%M:%S"))