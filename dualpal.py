"""
ID: ericbao2
LANG: PYTHON3
TASK: dualpal
"""
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

data = fin.read().split()
def convert(n, b):
    if b == 1:
        exit()
    l = 0
    re = []
    while n >= b**l:
        l += 1

    for i in reversed(range(l)):
        a = n // (b**i)

        if a < 10:
            a = str(a)
        else:
            a = chr(ord('A')+a-10)
        re.append(a)
        n %= (b**i)
    re = ''.join(re)
    return re


outpt = []
for i in range(int(data[1])+1, 100000):
    a = 0
    for b in range(2,11):
        re = convert(i,b)
        if re == re[::-1]:
            a += 1
        if a >= 2:
            outpt.append(i)
            break
    if len(outpt) >= int(data[0]):
        break

for i in outpt:
    fout.write(str(i) +'\n')
fout.close()
fin.close()
