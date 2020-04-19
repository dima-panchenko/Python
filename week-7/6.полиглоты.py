u = set()
common = set()
first = int(input())
for i in range(first):
    empty = set()
    num_lang = int(input())
    for j in range(num_lang):
        empty.add(input())
        u |= empty
    if i == 0:
        common = empty
    else:
        common &= empty
print(len(common))
for i in common:
    print(i)
print(len(u))
for i in u:
    print(i)