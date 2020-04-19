infile = open("input.txt", "r", encoding="utf8")
a = []
for i in infile:
    a.append(i.split())
infile.close()
a.sort(key=lambda x: x[0])
outfile = open("output.txt", "w", encoding="utf8")
for b in a:
    b = [b[0], b[1], b[-1]]
    print(' '.join(map(str, b)), end='\n', file=outfile)
outfile.close()
