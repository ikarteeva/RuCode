import itertools

f = open('input.txt', 'r')

s = f.readline().split()
n = int(s[1])

result = f.readline().split()

mnozh = [int(item) for item in result] 

koef = abs(mnozh[0]+mnozh[1]+mnozh[2] - n)

kortezh = tuple()

for i in itertools.combinations(mnozh, 3):
  prob = abs(i[0]+i[1]+i[2]-n) 
  if (prob < koef):
    koef = prob
    kortezh = i

kortezh = sorted(kortezh)

print(*kortezh, sep=' ')

f.close()
