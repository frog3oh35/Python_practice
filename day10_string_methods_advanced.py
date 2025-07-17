### 2025-07-17 문자열 처리 심화

sentence = "파이선은 정말 재미있는 언어입니다. 파이썬 최고!"

# replace
print("💞 replace:", sentence.replace("파이썬", "Python"))

# count
print("🐇 count:", sentence.count("파이썬"))

# find
print("🔍 find:", sentence.find("재미")) #시작 위치
print("🔍 find (없는 단어):", sentence.find("자바")) # 없으면 -1

#join
words = ["파이썬", "자바", "c++"]
joined = ", ".join(words)
print("📎 join:", joined)

print()

name = "연하"
age = 27

# f-string (추천 방식)
print(f"안녕하세요, 저는 {name}이고 나이는 {age}입니다.")

# .format()
print("안녕하세요, 저는 {}이고 나이는 {}입니다.".format(name, age))

# % 방식
print("안녕하세요, 저는 %s이고 나이는 %d입니다." % (name, age))