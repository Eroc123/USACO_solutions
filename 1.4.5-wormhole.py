"""
ID: ericbao2
LANG: PYTHON3
TASK: wormhole
"""

fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
data = fin.read().split('\n')
amount = int(data[0])
cords = []
for i in range(1,amount+1):
    x,y = data[i].split()
    cords.append((x,y))
print(cords)
i = 0
pared = []
x,y = cords[0]
for i in range(1,amount):


    px,py = cords[i]
    pared.append((x,y,px,py))
print(pared)
