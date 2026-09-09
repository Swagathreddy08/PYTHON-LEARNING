scores = [85, 92, 76, 88]
print(scores[0]) # 85
print(scores[2]) # 76
print(scores[-1]) # 88
print(scores[-2]) # 76

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30]
print(numbers[2:]) # [30, 40, 50]
print(numbers[::2]) # [10, 30, 50]
print(numbers[::-1]) # reversed copy

a = [10, 20, 30]
b = a.copy()
# or: b = a[:]
b.append(40)
print(a)
print(b)