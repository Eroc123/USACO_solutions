"""
ID: ericbao2
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
data = fin.read().split('\n')
people = {}
for i in range(int(data[0])):
    people[data[i+1]] = 0
def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return int(i)

offset = int(data[0])
for i in range(int(data[0])):
    print()
    print(offset)
    print(people)
    gifter = data[offset+1]
    amount = int(data[offset+2].split()[0])
    ng = int(data[offset+2].split()[1])
    print(gifter, amount, ng)
    people[gifter] -= amount
    if ng == 0:
        offset += ng + 2
        continue
    for i in range(ng):
        people[data[offset+3+i]] += truncate(amount/ng, 0)
        print(f'{data[offset+3+i]} +{truncate(amount/ng, 0)}')

    people[gifter] += amount % ng

    offset += ng + 2
print(people)
for i in people:
    fout.write(f'{i} {people[i]}\n')
fout.close()
