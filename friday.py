"""
ID: ericbao2
LANG: PYTHON3
TASK: friday
"""
fin = open('friday.in','r')
N = int(fin.readline())
def leap(y):
    return y % 400 == 0 or (y % 100 != 0 and y % 4== 0)


weeks = {i : 0 for i in range(7)}
months = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 0
for y in range(1900,1900+N):
	for m in months:
		weeks[day % 7] += 1
		if m == 28:
			if leap(y):
				day += 29
				continue
		day += m
with open('friday.out','w') as fout:
	for day in range(6):
		fout.write("{} ".format(weeks[day]))
	fout.write("{}\n".format(weeks[6]))
