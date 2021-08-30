"""
ID: ericbao2
LANG: PYTHON3
TASK: palsquare
"""

fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')
b = int(fin.read())

def convert(n, b):
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

for n in range(1,100000):
    bsqr = convert(n**2, b)
    if bsqr == bsqr[::-1]:
        fout.write(convert(n, b) + ' ' + bsqr + '\n')
