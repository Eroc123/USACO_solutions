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

if int(m)-1 == 0:
    fout.write(str(max(cows)-min(cows)+1)+'\n')
    exit()
for i in range(int(m)-1):
    largegaps += spaces.pop()-1
    print(largegaps)
print(largegaps)
fout.write(str(max(cows)-min(cows)-largegaps+1))
fout.write('\n')
