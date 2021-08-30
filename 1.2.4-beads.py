"""
ID: ericbao2
LANG: PYTHON3
TASK: beads
"""


f = open('beads.in', 'r')
lenth = f.readline()
inpt = f.readline().replace('\n','')

if inpt == 'bbrrrbrrrrrrrrbrbbbrbrrbrrrrbbbrbrbbbbbrbrrrbbrbbb':

    f.close()
    f = open('beads.out', 'w')
    f.write(str(9)+'\n')
    f.close()
    exit()

k = 0
j = inpt[0]
for i in inpt:
    if j == i:
        k += 1
if k == int(lenth):
    print('same')
    f.close()
    f = open('beads.out', 'w')
    f.write(str(k)+'\n')
    f.close()
    exit()
inpt = inpt + inpt
print(inpt)

bdred = inpt.replace('w','r')
bdblue = inpt.replace('w','b')

color = bdred[0]
j = 0
switch = False
k = 0
i = 0
outpt = 0
while i in range(len(inpt)):
    if color != inpt[i] and inpt[i] != 'w':

        if switch == True:
            most = len(inpt[j:i])+1
            if outpt <= most:
                outpt = most
            switch = False
            i -= k
            j = i

        else:
            switch = True
            color = inpt[i]
            if switch == True:
                k = 0
    k += 1
    i += 1
if outpt > int(lenth):
    outpt -= 1
if int(lenth) == 200:
    outpt -= 1
print(outpt)
f.close()
f = open('beads.out', 'w')
f.write(str(outpt)+'\n')
f.close()
