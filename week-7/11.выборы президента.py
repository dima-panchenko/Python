inf = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")
tex = inf.read().splitlines()
nowDict = {}
for i in tex:
    nowDict[i] = nowDict.get(i, 0) + 1
res = sorted(nowDict.items(), key=lambda x: (-x[1]))
if res[0][1] > len(tex) / 2:
    print(res[0][0], file=fout)
else:
    print(res[0][0], file=fout)
    print(res[1][0], file=fout)
inf.close()
fout.close()
