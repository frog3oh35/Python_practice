# comprehension, map, lambda, zip 복습...
print("🐰💻 Comprehension + map + lambda + zip 💌 \n")

print("baisc comprehension: Even numbers squared")
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)

print("\nmap + lambda: Add 10 using map + lambda")
numbers = [1, 2, 3, 4, 5]
plus_ten = list(map(lambda x : x + 10, numbers))
print(plus_ten)

print("\nfilter + lambda: kepp only multiples of 3 🐰")
filterd = list(filter(lambda x : x % 3 == 0, range(1, 11)))
print(filterd)

print("\nConvert to lowercase and get lengths 🐇🐇")
words = ["Rabbit", "Bunny", "Tokki"]
lengths = [len(w) for w in map(lambda x : x.lower(), words)]
print(lengths)

print("\nSquare all elements in a 2D list")
matrix = [[1, 2, 3], [4, 5, 6]]
flattened_squared = [x**2 for row in matrix for x in row]
print("Result:", flattened_squared)
flattened_squared_map = list(map(lambda x : x**2, [n for row in matrix for n in row]))
print("Map version:", flattened_squared_map, "\n")

print("zip + map + lambda: Add two lists using zip + map + lambda 🥕")
a = [1, 2, 3]
b = [10, 20, 30]
summed = list(map(lambda x, y: x + y, a, b))
print("Result:", summed, "\n")

print("Combine filter, map, and comprehension")
words = ["cat", "RABBIT", "turtle", "dog", "elephant"]
result = [len(w) for w in map(lambda x : x.upper(), filter(lambda x: len(x) >= 4, words))]
print("Result:", result, "\n")

print("🐇✨🐰🥕💖")