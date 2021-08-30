"""
ID: ericbao2
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
data = fin.read().split('\n')
ns = []
for i in range(1,int(data[0])+1):
    ns.append(i)

solutions = []
#print(data)
#print(int(data[1].split()[2])+2)
for i in range(int(data[1].split()[0])-3,int(data[1].split()[0])+2):
    for j in range(int(data[1].split()[1])-3,int(data[1].split()[1])+2):
        for k in range(int(data[1].split()[2])-3,int(data[1].split()[2])+2):
            try:
                solutions.append(str([ns[i],ns[j],ns[k]]))
            except:
                pass
for i in range(int(data[2].split()[0])-3,int(data[2].split()[0])+2):
    for j in range(int(data[2].split()[1])-3,int(data[2].split()[1])+2):
        for k in range(int(data[2].split()[2])-3,int(data[2].split()[2])+2):
            try:
                solutions.append(str([ns[i],ns[j],ns[k]]))
            except:
                pass

solutions = list(dict.fromkeys(solutions))
#print(solutions)
#print(len(solutions))
fout.write(str(len(solutions))+'\n')
