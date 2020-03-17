num = int(input())
i = 1
fib = 0
pre1 = 1
pre2 = 0
while i < num:
    fib = pre1 + pre2
    pre2 = pre1
    pre1 = fib
    i += 1
if num == 1:
    print(1)
else:
    print(fib)
