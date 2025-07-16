### 2025-07-16 파일 입출력

"""
## 텍스트 파일 쓰기
f = open("hello.txt", "w", encoding="utf-8")
f.write("안녕하세요!\n")
f.write("파일 입출력을 배우는중. \n")
f.close()
# `w`는 기존 파일이 있으면 덮어쓰기, 없으면 새로 생성한다.
"""

## 파일 읽기
f = open("hello.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

"""
## 줄 단위로 읽기
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readline()
    for line in lines:
        print(line.strip())
        # 줄바꿈 제거하고 출력
"""

## 이어쓰기
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("이 내용은 기존 파일에 이어서 추가됩니다.")