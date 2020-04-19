import sys
text = sys.stdin.read()
textSpl = text.split()
mySet = set(textSpl)
print(len(mySet))
