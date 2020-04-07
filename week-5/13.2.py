a = list(map(str, input().split()))
MaxEl = 0
MinEl = 0
for i in range(1, len(a)):
    if a[i] > a[MaxEl]:
        MaxEl = i
    elif a[i] < a[MinEl]:
        MinEl = i
a[MaxEl], a[MinEl] = a[MinEl], a[MaxEl]
print(' '.join(a))
