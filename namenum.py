"""
ID: ericbao2
LANG: PYTHON3
TASK: namenum
"""

with open('namenum.in','r') as fin:
    tags = fin.read()[:-1]
with open('dict.txt','r') as fin:
    names = fin.read().split('\n')

def toNum(c):
    num = ord(c)-65
    for i in range(1,9):
        if ord(c) < ord('Q'):
            if num < i*3:
                return str(i+1)
        else:
            if num < i*3+1:
                return str(i+1)
    print(c, num)

for i in range(65,89):
    print(toNum(chr(i)), chr(i))
le = len(tags)
outpt = []
for name in names:
    if len(name) != le:
        continue
    if 'Z' in name:
        continue
    if 'Q' in name:
        continue
    tag = ''
    for i in name:
        tag += toNum(i)
    if tags == tag:
        outpt.append(name)
print(outpt)

















if len(outpt) == 0:
    outpt.append('NONE')
with open('namenum.out','w') as fout:
    for i in outpt:
        fout.write(i+'\n')
