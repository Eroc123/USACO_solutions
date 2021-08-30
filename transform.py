"""
ID: ericbao2
LANG: PYTHON3
TASK: transform
"""
from copy import *
global data

def printsh(shape):
    for i in shape:
        print(i)
    print()
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
data = fin.read().split('\n')
fin.close()
oshape = []
cshape = []
for i in range(1,int(data[0])+1):
    oshape.append(list(data[i]))
for i in range(1+int(data[0]),int(data[0])*2+1):
    cshape.append(list(data[i]))


def rotate(shape):
    result = []
    result = deepcopy(shape)
    side = int(data[0])
    for i in range(side):

        k = 0
        for j in shape[i]:

            result[k][(i+1)*-1] = j
            k += 1

    return result
def reflect(shape):

    result = deepcopy(shape)
    for i in range(len(result)):
        result[i].reverse()
    return result

tshape = deepcopy(oshape)
#detection

tr = 0

if tshape == cshape:
    tr = 6
for i in range(1,4):
    tshape = rotate(tshape)
    printsh(tshape)
    if tshape == cshape:
        tr = i
        break
if tr == 0:
    tshape = reflect(oshape)
    if tshape == cshape:
        tr = 4
    else:
        for i in range(1,4):
            tshape = rotate(tshape)
            if tshape == cshape:
                tr = 5
            else:
                pass

if tr == 0:
    tr = 7
fout.write(f'{tr}\n')
fout.close()
