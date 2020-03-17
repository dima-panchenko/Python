p = int(input())
x = int(input())
y = int(input())
dep = x * 100 + y
per = dep * (p / 100)
total = dep + per
print(int(total / 100), int(total % 100))
