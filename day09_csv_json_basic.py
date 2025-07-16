### 2025-07-16 CSV & JSON 처리 기본
import csv
import json

## CSV 파일 쓰기
"""
with open("data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "직업"])
    writer.writerow(["연하", 27, "학생"])
    writer.writerow(["지민", 30, "개발자"])
"""
## 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


## JSON 파일 쓰기
"""
data = {
    "이름" : "연하",
    "나이" : 27,
    "관심" : ["QA", "DevOps", "클라우드"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
"""
# ensure_ascii 한글 깨짐 방지
# indent= 2 예쁘게 정렬

## JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print(loaded["관심"])