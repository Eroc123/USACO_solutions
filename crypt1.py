"""
ID: ericbao2
LANG: PYTHON3
TASK: crypt1
"""
global n
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
data = fin.read().split('\n')
lenth = len(data[0])
n = data[1].split()

def multiply(x,y):
    x = str(x)
    y = str(y)
    if len(x) != 3:
        return False
    if len(y) != 2:
        return False
    j = 0
    re = 0
    for i in y:
        p = int(x) * int(i)*(10**j)
        for k in str(p)[0:3]:
            if not k in n:
                return False
        if len(str(p)) != 3+j:
            return False
        #print(p)
        re += int(p)
        j += 1

    if len(str(re)) != 4:
        return False
    for i in str(re):
        if not i in n:
            return False
    #print(re, x,y)
    return True
outpt = 0
for i in n:
    for j in n:
        for k in n:
            for l in n:
                for m in n:
                    if multiply(int(i+j+k), int(l+m)):
                        outpt += 1
fout.write(str(outpt) + '\n')
