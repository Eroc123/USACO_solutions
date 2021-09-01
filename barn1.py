"""
ID: ericbao2
LANG: PYTHON3
TASK: barn1
"""
fin = open ('barn1.in', 'r')

fout = open ('barn1.out', 'w')
data = fin.read().split('\n')
fin.close()
m,sta,occ = data[0].split()
cows = []
for i in range(1,int(occ)+1):
    cows.append(int(data[i]))
if int(m) > int(occ):
    fout.write(occ)
    fout.write('\n')
    exit()
cows.sort()
spaces = []
for i in range(int(occ)-1):
    spaces.append(int(cows[i+1]) - int(cows[i]))
spaces.sort()
largegaps =0
print(cows)

spaces = spaces[::-1]
print(spaces)
if int(m)-1 == 1:
    largegaps = 1
if int(m)-1 == 0:
    fout.write(str(max(cows)-min(cows)+1)+'\n')
    exit()
for i in range(int(m)-1):
    largegaps += (spaces[i])
    print(spaces[i])
print(largegaps)
fout.write(str(max(cows)-largegaps+1))
fout.write('\n')
exit()

print(cows)
outpt = 0
if m > occ:
    outpt = occ
spaces = []
for i in range(int(occ)-3):
    spaces.append(int(cows[i+1]) - int(cows[i]) - 1)
spaces.sort()
print(spces)
gap = 0
for i in range(int(m)-1):
    gap += spaces[i*-1]
outpt = max(cows) - min(cows) + 1 - gap
fout.write(str(outpt-3))
fout.write('\n')
