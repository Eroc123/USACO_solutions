"""
ID: ericbao2
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
data = fin.read().split('\n')
indexs = {}
sorted = []


for i in data[1:-1]:
    j = i.split()
    try:
        indexs[int(str(j[0]))]+= int(j[1])
    except KeyError:
        indexs[int(str(j[0]))] = int(j[1])
        sorted.append(int(str(j[0])))
        continue




sorted.sort()
price = 0
total = int(data[0].split()[0])
for i in sorted:
    print(i, indexs[i])
for i in sorted:
    if total >= indexs[i]:
        total -= indexs[i]
        price += i * indexs[i]
        print(i, indexs[i], total, price)
        if total == 0:
            break
    else:
        price += i* (total)
        print(price)
        total = 0
        break
fout.write(str(price)+'\n')
fout.close()
fin.close()
