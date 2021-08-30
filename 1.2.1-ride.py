"""
ID: ericbao2
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
def convert(name):
    number = 1
    for i in list(name):
        number *= ord(i)-64
    return number
data = fin.read()
data = data.split('\n')
x = convert(data[0]) % 47
y = convert(data[1]) % 47
if x == y:
    fout.write('GO\n')
else:
    fout.write('STAY\n')
fout.close()
