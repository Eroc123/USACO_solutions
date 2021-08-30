"""
ID: ericbao2
LANG: PYTHON3
TASK: milk2
"""

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')



data = fin.read().split('\n')
if len(data) == 3:
    fout.write(f'{int(data[1].split()[1]) - int(data[1].split()[0])} {0}\n')
    fout.close()
    exit()
indexs = []
listmax = []
listnum = []
for i in data[1:-1]:
    datasub = i.split()
    datasub = [int(datasub[0]), int(datasub[1])]
    listnum.append([datasub[0],datasub[1]])
milk , pause = [],[]



for i in listnum:

    milk.append(i[0])
    pause.append(i[1])
milk.sort()
pause.sort()
listnum = []
for x in range(len(milk)):
    listnum.append([milk[x], pause[x]])


listnum = []
for x in range(len(milk)):
    listnum.append([milk[x], pause[x]])
print(listnum)
j = listnum[0]
listmin = []

for i in listnum:
    print(i[0], j[1])
    if i[0] <= j[1]:
        i[0] = j[0]
    listmax.append(i[1] - i[0])
    listmin.append(i[0] - j[1])

    j = i

print(listmax, listmin)
if max(listmin) < 0:
    listmin.append(0)
fout.write(f'{max(listmax)} {max(listmin)}\n')
fout.close()
