p = int(input())
x = int(input())
y = int(input())
k = int(input())
dep = x * 100 + y
per = dep * (p / 100)
i = 0
total = 0
while i < k:
    per = dep * (p / 100)
    total = dep + per
    dep = int(total)
    i += 1
print(int(total / 100), int(total % 100))
