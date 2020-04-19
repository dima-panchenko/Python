import collections
with open('input.txt', 'r', encoding='utf8') as d:
    k = list(d.read().split())  # считали текст в список по словам
g = (collections.Counter(k)).most_common()
g.sort(key=lambda x: (-x[1], x[0]))
for element in g:
    print(element[0])